# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
import logging

from hmv_widget import Ui_HmvWidget
from hmv_meretezes import NetworkEnvironment, AnalyzeHeatLoss, AnalyzeFlowRate
from hmv_meretezes_models import SizeListModel, ElementErrorTableModel
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
    # Default settings
    self.sizes = [10, 12, 16, 19, 25, 32, 40]
    self.density = 983.2 # kg/m3
    self.specificHeat = 4200.0 # J/kgK
    self.deltaTheta = 2.0 # K

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
    self.sizeListModel = SizeListModel(self.sizes)
    self.elementErrTableModel = ElementErrorTableModel()
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
    QObject.connect(self.dock.heatlossStart_btn, SIGNAL("clicked()"), self.startHeatlossCalc)
    QObject.connect(self.dock.flowRateStart_btn, SIGNAL("clicked()"), self.startFlowCalc)
    QObject.connect(self.dock.validateStart_btn, SIGNAL("clicked()"), self.startNetworkValidation)
    QObject.connect(self.dock.addSize_btn, SIGNAL("clicked()"), self.addSizeToList)
    QObject.connect(self.dock.removeSize_btn, SIGNAL("clicked()"), self.removeSizeFromList)
    QObject.connect(self.dock.saveSettings_btn, SIGNAL("clicked()"), self.saveSettings)
    QObject.connect(self.dock.resetSettings_btn, SIGNAL("clicked()"), self.setDefaultValues)
  def setDefaultValues(self):
    self.dock.density_txtField.setText(str(self.density))
    self.dock.specificHeat_txtField.setText(str(self.specificHeat))
    self.dock.deltaTheta_txtField.setText(str(self.deltaTheta))
  def saveSettings(self):
    self.density = float(self.dock.density_txtField.text())
    self.specificHeat = float(self.dock.specificHeat_txtField.text())
    self.deltaTheta = float(self.dock.deltaTheta_txtField.text())
  def addSizeToList(self):
    value = self.dock.insertSize_txtField.text()
    self.sizeListModel.insertRows(value)
  def removeSizeFromList(self):
    selected = self.dock.sizeList.selectedIndexes()
    for selection in selected:
      self.sizeListModel.removeRows(selection)
  def startNetworkValidation(self):
      self.netEnv = NetworkEnvironment()
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
    self.dock.totalHeatloss_label.setText(str(anaHeat.totalNetworkHeatloss))
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
    