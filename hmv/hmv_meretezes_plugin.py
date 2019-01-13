# -*- coding: utf-8 -*-
from PyQt4.QtCore import Qt, QObject, SIGNAL # pylint: disable=E0611
from PyQt4.QtGui import QAction, QMessageBox # pylint: disable=E0611
import qgis.core
import logging
import os
import ConfigParser

from hmv_widget import Ui_HmvWidget
from hmv_results import Ui_result_widget
from hmv_chart import Ui_pipeFlowChart_wdg
from chart import PipeFlowChartCanvas
from hmv_meretezes import NetworkEnvironment, AnalyzeHeatLoss, AnalyzeFlowRate,\
                          AnalyzePipeDiameter, AnalyzePipeDrag, AnalyzePressure
from hmv_meretezes_models import SizeListModel, ElementErrorTableModel, ResultsTableModel,\
                                 PressureTableModel
import hmv_symbol_manager
import datasource_manager
from qt_utility import QtTranslate
# initialize Qt resources from file resouces.py
# import resources

class HmvPlugin(QObject):
    """Plugin object to initialize pipe network
    analyzer as a QGIS plugin
    """
    def __init__(self, iface):
        super(HmvPlugin, self).__init__()
        self.iniConfig = ConfigParser.ConfigParser()
        self.iniConfig.readfp(open(os.path.join(qgis.core.QgsApplication.qgisSettingsDirPath(),
                                                'python/plugins/hmv/hmv.ini')))
        # Reference to the QGIS Qt environment
        self.iface = iface
        self.dock = None
        self.stPluginAction = None
        # Setting up the application log
        self.configureLogging()
        # Used to store the network environment once initialized
        self.netEnv = None
        # Model for GUI size list
        self.sizeListModel = None
        self.resultsWin = None
        self.resultsModel = None
        self.pressureResultsWin = None
        self.pressureResultsModel = None
        self.chartWin = None
        self.elementErrTableModel = None
    def initGui(self):
        # create Qt action that will open the plugin
        self.stPluginAction = QAction(u"HMV Méretezés", self.iface.mainWindow()) # pylint: disable=E0602
        self.stPluginAction.setObjectName("pipeAnalyticsStart")
        self.stPluginAction.setWhatsThis("Option to start pipe network analysis")
        self.stPluginAction.setStatusTip(u"Méretező plugin indítása")
        # We run the widget when the action is triggered
        QObject.connect(self.stPluginAction, SIGNAL("triggered()"), self.startPlugin) # pylint: disable=E1101

        # add toolbar button and menu item
        # self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u'HMV Méretezés', self.stPluginAction)
    def unload(self):
        self.iface.removePluginMenu(u'HMV Méretezés', self.stPluginAction)
        QObject.disconnect(self.stPluginAction, SIGNAL("triggered()"), self.startPlugin) # pylint: disable=E1101
    def startPlugin(self):
        # We set up the network environment
        self.netEnv = NetworkEnvironment()
        # Instantiate the models required for view objects
        self.sizeListModel = SizeListModel(self.netEnv.sizes)
        self.elementErrTableModel = ElementErrorTableModel()
        # Instantiate the UI object
        self.dock = Ui_HmvWidget()
        self.dock.setupUi(self.dock)
        self.dock.sizeList.setModel(self.sizeListModel)
        self.dock.errElements_table.setModel(self.elementErrTableModel)
        # Analysis buttons are disabled by default
        self.dock.theAnalysis_btn.setEnabled(False)
        # We add the dock widget to the QGIS window
        self.iface.addDockWidget(Qt.RightDockWidgetArea, self.dock)
        self.setDefaultValues()
        self.bindConnections()
    def bindConnections(self):
        """Binds actions to GUI object signals"""
        # Analysis actions
        QObject.connect(self.dock.validateStart_btn, SIGNAL("clicked()"), self.startNetworkValidation) # pylint: disable=E1101
        QObject.connect(self.dock.theAnalysis_btn, SIGNAL("clicked()"), self.startAllCalc) # pylint: disable=E1101
        # Settings
        QObject.connect(self.dock.addSize_btn, SIGNAL("clicked()"), self.addSizeToList) # pylint: disable=E1101
        QObject.connect(self.dock.removeSize_btn, SIGNAL("clicked()"), self.removeSizeFromList) # pylint: disable=E1101
        QObject.connect(self.dock.saveSettings_btn, SIGNAL("clicked()"), self.saveSettings) # pylint: disable=E1101
        QObject.connect(self.dock.resetSettings_btn, SIGNAL("clicked()"), self.setDefaultValues) # pylint: disable=E1101
        QObject.connect(self.dock.circFlow_combo, SIGNAL("activated(int)"), self.refreshCircFlowDisplay) # pylint: disable=E1101
        # Result windows
        QObject.connect(self.dock.showResults_btn, SIGNAL("clicked()"), self.openResultsWindow) # pylint: disable=E1101
        QObject.connect(self.dock.showPressureResults_btn, SIGNAL("clicked()"), # pylint: disable=E1101
                        self.openPressureResultsWindow)
        QObject.connect(self.dock.showPipeFlowChart_btn, SIGNAL("clicked()"), self.openChartWindow) # pylint: disable=E1101
        # Layers
        QObject.connect(self.dock.refreshLayers_btn, SIGNAL("clicked()"), self.populateLayerChoice) # pylint: disable=E1101
        QObject.connect(self.dock.nodeLayerSelect_combo, SIGNAL("activated(QString)"), # pylint: disable=E1101
                        self.netEnv.setNodeLayerName)
        QObject.connect(self.dock.pipeLayerSelect_combo, SIGNAL("activated(QString)"), # pylint: disable=E1101
                        self.netEnv.setPipeLayerName)
        QObject.connect(self.dock.formatLayers_btn, SIGNAL("clicked()"), self.formatLayerChoice)
        QObject.connect(self.dock.createNewLayer_btn, SIGNAL('clicked()'), self.createNewLayer)
        QObject.connect(self.dock.autoDbFileName_checkbox, SIGNAL('stateChanged(int)'), self.dbLayerFileToggle)
        QObject.connect(self.dock.newLayerName_txtField, SIGNAL('editingFinished()'), self.autoSetDbLayerFileField)
    def startAllCalc(self):
        self.startHeatlossCalc()
        self.startFlowCalc()
        self.startPipeDiaCalc()
        self.startPipeDragCalc()
        self.startPressureCalc()
    def openResultsWindow(self):
        """Opens a new window with the analysis results like heatloss and related, results window #1"""
        self.resultsWin = Ui_result_widget()
        self.resultsWin.setupUi(self.resultsWin)
        self.resultsModel = ResultsTableModel(self.netEnv.generateResults())
        self.resultsWin.results_table.setModel(self.resultsModel)
        QObject.connect(self.resultsWin.closeWindow_btn, SIGNAL("clicked()"), self.resultsWin.close) # pylint: disable=E1101
        self.resultsWin.show() # pylint: disable=E1101
    def openPressureResultsWindow(self):
        """Opens a new windo with the analysis results like pressure loss, results window #2"""
        self.pressureResultsWin = Ui_result_widget()
        self.pressureResultsWin.setupUi(self.pressureResultsWin)
        self.pressureResultsModel = PressureTableModel(self.netEnv.generatePressureResults())
        self.pressureResultsWin.results_table.setModel(self.pressureResultsModel)
        QObject.connect(self.pressureResultsWin.closeWindow_btn, SIGNAL("clicked()"), # pylint: disable=E1101
                        self.pressureResultsWin.close) # pylint: disable=E1101
        self.pressureResultsWin.show() # pylint: disable=E1101
    def openChartWindow(self):
        self.chartWin = Ui_pipeFlowChart_wdg()
        self.chartWin.setupUi(self.chartWin)
        chart = PipeFlowChartCanvas(flowData=self.netEnv.generateFlowGraphResults(),
                                    parent=self.chartWin)
        self.chartWin.chartTarget_lo.addWidget(chart)
        self.chartWin.show() # pylint: disable=E1101
    def setDefaultValues(self):
        self.dock.density_txtField.setText(str(self.netEnv.density))
        self.dock.specificHeat_txtField.setText(str(self.netEnv.specificHeat))
        self.dock.deltaTheta_txtField.setText(str(self.netEnv.deltaTheta))
        self.dock.pipeSpeedLimit_txtField.setText(str(self.netEnv.pipeSpeedLimit))
        # New layer creation interface
        self.dock.layerWorkingDirectory_txtField.setText(self.iniConfig.get('hmv', 'workdir'))
        self.dock.newLayerDbFile_txtField.setReadOnly(False)
        # Working layer selection interface
        self.populateLayerChoice()
    def populateLayerChoice(self):
        # Populating layer choice combo
        self.dock.nodeLayerSelect_combo.clear()
        self.dock.nodeLayerSelect_combo.addItems(self.netEnv.collectLayers(qgis.core.QGis.WKBPoint))
        self.netEnv.setNodeLayerName(self.dock.nodeLayerSelect_combo.currentText())
        self.dock.pipeLayerSelect_combo.clear()
        self.dock.pipeLayerSelect_combo.addItems(self.netEnv.collectLayers(qgis.core.QGis.WKBLineString))
        self.netEnv.setPipeLayerName(self.dock.pipeLayerSelect_combo.currentText())
        
    def formatLayerChoice(self):
        hmv_symbol_manager.setupNodeLayer(self.dock.nodeLayerSelect_combo.currentText())
        hmv_symbol_manager.setupPipeLayer(self.dock.pipeLayerSelect_combo.currentText())
        self.iface.mapCanvas().refreshAllLayers()
    def saveSettings(self):
        self.netEnv.density = float(self.dock.density_txtField.text())
        self.netEnv.specificHeat = float(self.dock.specificHeat_txtField.text())
        self.netEnv.deltaTheta = float(self.dock.deltaTheta_txtField.text())
        self.netEnv.pipeSpeedLimit = float(self.dock.pipeSpeedLimit_txtField.text())
    def addSizeToList(self):
        value = self.dock.insertSize_txtField.text()
        self.sizeListModel.insertRows(value)
    def removeSizeFromList(self):
        selected = self.dock.sizeList.selectedIndexes()
        for selection in selected:
            self.sizeListModel.removeRows(selection)
    def startNetworkValidation(self):
        if self.netEnv.pipeLayerName != None and self.netEnv.nodeLayerName != None:
            self.netEnv.buildObjects()
            status = self.netEnv.verifyObjectConnections()
            self.dock.checkStatusValue_label.setText(
                QtTranslate('HmvWidget',
                            self.netEnv.statusCodes[status['overallStatus']],
                            None))
            self.dock.numberOfElementsValue_label.setText(str(status['allElementsCount']))
            self.dock.numberOfErrElementsValue_label.setText(str(status['errElementsCount']))
            self.elementErrTableModel.removeRows()
            self.elementErrTableModel.insertRows(status['errElements'])
            # If network validation is OK enable analysis buttons
            if status['overallStatus'] == 2:
                self.dock.theAnalysis_btn.setEnabled(True)
                self.dock.verifyNotification_lbl.setVisible(False)
        else:
            pass
    def startHeatlossCalc(self):
        anaHeat = AnalyzeHeatLoss(self.netEnv)
        logging.info('STAGE 1 | Starting heatloss analysis.' \
                      'Calculating network heatloss for the first nodes after taps first.')
        anaHeat.doAnalyze()
        logging.info('STAGE 2 | Analyze network heatlos on next nodes in network.')
        anaHeat.analyzeNextNodes()
        self.dock.totalHeatloss_label.setText('{:.1f}'.format(round(self.netEnv.totalNetworkHeatloss,
                                                                    1)))
        self.dock.circFlow_label.setText('{:.1f}'.format(round(self.netEnv.pumpFlow, 1)))
    def startFlowCalc(self):
        anaFlow = AnalyzeFlowRate(self.netEnv)
        logging.info('STAGE 1 | Starting flow rate analysis.' \
                      'Calculating network heatloss at the pump pipe first.')
        anaFlow.doAnalyze()
        logging.info('STAGE 2 | Analyze flow rate on next nodes in network.')
        anaFlow.analyzeNextNodes()
    def configureLogging(self):
        """Configures the logging env"""
        logging.basicConfig(filename=self.iniConfig.get("hmv", "logdir") + 'plugin.log',
                            level=logging.DEBUG,
                            format='%(asctime)s %(levelname)s:%(message)s')
    def startPipeDiaCalc(self):
        calcDia = AnalyzePipeDiameter(self.netEnv)
        calcDia.doAnalyze()
    def refreshCircFlowDisplay(self):
        logging.info('Flow dimension changed.')
        if self.dock.circFlow_combo.currentText() == 'm3/sec':
            self.dock.circFlow_label.setText(str(self.netEnv.pumpFlow / 3.6e6))
        elif self.dock.circFlow_combo.currentText() == 'dm3/h':
            self.dock.circFlow_label.setText(str(self.netEnv.pumpFlow))
    def startPipeDragCalc(self):
        calcDrag = AnalyzePipeDrag(self.netEnv)
        calcDrag.doAnalyze()
    def startPressureCalc(self):
        calcPress = AnalyzePressure(self.netEnv)
        calcPress.doAnalyze()


    def disableAnalysis(self):
        self.dock.theAnalysis_btn.setEnabled(False)
        self.dock.verifyNotification_lbl.setVisible(True)


    def autoSetDbLayerFileField(self):
        if self.dock.autoDbFileName_checkbox.isChecked() == True:
            self.dock.newLayerDbFile_txtField.setText('{}.sqlite'.format(
                                                            self.dock.newLayerName_txtField.text()
                                                      )
            )


    def dbLayerFileToggle(self, status):
        """Disable layer file name field if determined by layer name
        enable if not.
        """
        if status == Qt.Checked:
            self.autoSetDbLayerFileField()
            self.dock.newLayerDbFile_txtField.setReadOnly(True)
        elif status == Qt.Unchecked:
            self.dock.newLayerDbFile_txtField.setReadOnly(False)


    def createNewLayer(self):
        """Create a new datasource and layer, add to registry if needed"""
        try:
            dsPath = datasource_manager.createLayer(self.dock.newLayerName_txtField.text(),
                                           self.dock.newLayerDbFile_txtField.text(),
                                           self.dock.layerWorkingDirectory_txtField.text(),
                                           self.dock.newLayerType_combo.currentText())
        except OSError as err:
            # Working dir doesn't exist or datasource file exists
            mBox = QMessageBox()
            mBox.setText('Datasource error: {}'.format(err))
            mBox.setIcon(QMessageBox.Critical)
            mBox.exec_()
        else:
            if self.dock.newLayerAddToRegistry_checkbox.isChecked() == True:
                uri = qgis.core.QgsDataSourceURI()
                uri.setDatabase(dsPath)
                schema = ''
                table = self.dock.newLayerName_txtField.text()
                geom_column = 'GEOMETRY'
                uri.setDataSource(schema, table, geom_column)

                display_name = self.dock.newLayerName_txtField.text()
                vlayer = qgis.core.QgsVectorLayer(uri.uri(), display_name, 'spatialite')
                qgis.core.QgsMapLayerRegistry.instance().addMapLayer(vlayer)
