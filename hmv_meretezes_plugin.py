# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
import logging

from hmv_widget import Ui_HmvWidget
from hmv_results import Ui_result_widget
from hmv_chart import Ui_pipeFlowChart_wdg
from chart import PipeFlowChartCanvas
from hmv_meretezes import NetworkEnvironment, AnalyzeHeatLoss, AnalyzeFlowRate, AnalyzePipeDiameter, AnalyzePipeDrag, AnalyzePressure
from hmv_meretezes_models import SizeListModel, ElementErrorTableModel, ResultsTableModel, PressureTableModel
from qt_utility import QtTranslate
# initialize Qt resources from file resouces.py
# import resources

class HmvPlugin(QObject):
  """Plugin object to initialize pipe network
  analyzer as a QGIS plugin
  """
  def __init__(self, iface):
    super(HmvPlugin, self).__init__()
    # Reference to the QGIS Qt environment
    self.iface = iface
    # Setting up the application log
    self.configureLogging()
    # Used to store the network environment once initialized
    self.netEnv = None
    # Model for GUI size list
    self.sizeListModel = None

  def initGui(self):
    # create Qt action that will open the plugin
    self.stPluginAction = QAction("HMV Meretezes", self.iface.mainWindow())
    self.stPluginAction.setObjectName("pipeAnalyticsStart")
    self.stPluginAction.setWhatsThis("Option to start pipe network analysis")
    self.stPluginAction.setStatusTip("Meretezo plugin inditasa")
    # We run the widget when the action is triggered
    QObject.connect(self.stPluginAction, SIGNAL("triggered()"), self.startPlugin)

    # add toolbar button and menu item
    # self.iface.addToolBarIcon(self.action)
    self.iface.addPluginToMenu("HMV Meretezes", self.stPluginAction)
  def unload(self):
    self.iface.removePluginMenu("HMV Meretezes", self.stPluginAction)
    QObject.disconnect(self.stPluginAction, SIGNAL("triggered()"), self.startPlugin)
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
    self.dock.heatlossStart_btn.setEnabled(False)
    self.dock.flowRateStart_btn.setEnabled(False)
    # We add the dock widget to the QGIS window
    self.iface.addDockWidget( Qt.RightDockWidgetArea, self.dock )
    self.setDefaultValues()
    self.bindConnections()
  def bindConnections(self):
    """Binds actions to GUI object signals"""
    # Analysis actions
    QObject.connect(self.dock.heatlossStart_btn, SIGNAL("clicked()"), self.startHeatlossCalc)
    QObject.connect(self.dock.flowRateStart_btn, SIGNAL("clicked()"), self.startFlowCalc)
    QObject.connect(self.dock.validateStart_btn, SIGNAL("clicked()"), self.startNetworkValidation)
    QObject.connect(self.dock.returnPipeDiaStart_btn, SIGNAL("clicked()"), self.startPipeDiaCalc)
    QObject.connect(self.dock.pipeDragStart_btn, SIGNAL("clicked()"), self.startPipeDragCalc)
    QObject.connect(self.dock.pressureLossStart_btn, SIGNAL("clicked()"), self.startPressureCalc)
    QObject.connect(self.dock.theAnalysis_btn, SIGNAL("clicked()"), self.startAllCalc)
    # Settings
    QObject.connect(self.dock.addSize_btn, SIGNAL("clicked()"), self.addSizeToList)
    QObject.connect(self.dock.removeSize_btn, SIGNAL("clicked()"), self.removeSizeFromList)
    QObject.connect(self.dock.saveSettings_btn, SIGNAL("clicked()"), self.saveSettings)
    QObject.connect(self.dock.resetSettings_btn, SIGNAL("clicked()"), self.setDefaultValues)
    QObject.connect(self.dock.circFlow_combo, SIGNAL("activated(int)"), self.refreshCircFlowDisplay)
    # Result windows
    QObject.connect(self.dock.showResults_btn, SIGNAL("clicked()"), self.openResultsWindow)
    QObject.connect(self.dock.showPressureResults_btn, SIGNAL("clicked()"), self.openPressureResultsWindow)
    QObject.connect(self.dock.showPipeFlowChart_btn, SIGNAL("clicked()"), self.openChartWindow)
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
    QObject.connect(self.resultsWin.closeWindow_btn, SIGNAL("clicked()"), self.resultsWin.close)
    self.resultsWin.show()
  def openPressureResultsWindow(self):
    """Opens a new windo with the analysis results like pressure loss, results window #2"""
    self.pressureResultsWin = Ui_result_widget()
    self.pressureResultsWin.setupUi(self.pressureResultsWin)
    self.pressureResultsModel = PressureTableModel(self.netEnv.generatePressureResults())
    self.pressureResultsWin.results_table.setModel(self.pressureResultsModel)
    QObject.connect(self.pressureResultsWin.closeWindow_btn, SIGNAL("clicked()"), self.pressureResultsWin.close)
    self.pressureResultsWin.show()
  def openChartWindow(self):
    self.chartWin = Ui_pipeFlowChart_wdg()
    self.chartWin.setupUi(self.chartWin)
    chart = PipeFlowChartCanvas(flowData=self.netEnv.generateFlowGraphResults(), parent=self.chartWin)
    self.chartWin.chartTarget_lo.addWidget(chart)
    self.chartWin.show()
  def setDefaultValues(self):
    self.dock.density_txtField.setText(str(self.netEnv.density))
    self.dock.specificHeat_txtField.setText(str(self.netEnv.specificHeat))
    self.dock.deltaTheta_txtField.setText(str(self.netEnv.deltaTheta))
    self.dock.pipeSpeedLimit_txtField.setText(str(self.netEnv.pipeSpeedLimit))
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
      status = self.netEnv.verifyObjectConnections()
      self.dock.checkStatusValue_label.setText(QtTranslate('HmvWidget', self.netEnv.statusCodes[status['overallStatus']], None))
      self.dock.numberOfElementsValue_label.setText(str(status['allElementsCount']))
      self.dock.numberOfErrElementsValue_label.setText(str(status['errElementsCount']))
      self.elementErrTableModel.removeRows()
      self.elementErrTableModel.insertRows(status['errElements'])
      # If network validation is OK enable analysis buttons
      if status['overallStatus'] == 2:
        self.dock.heatlossStart_btn.setEnabled(True)
        self.dock.flowRateStart_btn.setEnabled(True)
  def startHeatlossCalc(self):
    anaHeat = AnalyzeHeatLoss(self.netEnv)
    logging.info('STAGE 1 | Starting heatloss analysis.' \
                  'Calculating network heatloss for the first nodes after taps first.')
    anaHeat.doAnalyze()
    logging.info('STAGE 2 | Analyze network heatlos on next nodes in network.')
    anaHeat.analyzeNextNodes()
    self.dock.totalHeatloss_label.setText(str(self.netEnv.totalNetworkHeatloss))
    self.dock.circFlow_label.setText(str(self.netEnv.pumpFlow))
  def startFlowCalc(self):
    anaFlow = AnalyzeFlowRate(self.netEnv)
    logging.info('STAGE 1 | Starting flow rate analysis.' \
                  'Calculating network heatloss at the pump pipe first.')
    anaFlow.doAnalyze()
    logging.info('STAGE 2 | Analyze flow rate on next nodes in network.')
    anaFlow.analyzeNextNodes()
  def configureLogging(self):
    """Configures the logging env"""
    logging.basicConfig(filename='/Users/cruizer/Documents/kristofQgis/plugin.log',
                        level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s:%(message)s')
  def startPipeDiaCalc(self):
    calcDia = AnalyzePipeDiameter(self.netEnv)
    calcDia.doAnalyze()
  def refreshCircFlowDisplay(self, index):
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
