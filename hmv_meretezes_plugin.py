from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
import logging

from hmv_widget import Ui_HmvWidget
from hmv_meretezes import NetworkEnvironment, AnalyzeHeatLoss
from hmv_meretezes_models import SizeListModel
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
    sizes = [10, 12.5, 16, 19, 25, 32, 40]
    self.sizeListModel = SizeListModel(sizes)
    self.dock = Ui_HmvWidget()
    self.dock.setupUi(self.dock)
    self.dock.sizeList.setModel(self.sizeListModel)
    self.iface.addDockWidget( Qt.RightDockWidgetArea, self.dock )
    self.bindConnections()
  def bindConnections(self):
    QObject.connect(self.dock.heatlossStart_btn, SIGNAL("clicked()"), self.startHeatlossCalc)
    QObject.connect(self.dock.validateStart_btn, SIGNAL("clicked()"), self.startNetworkValidation)
    QObject.connect(self.dock.addSize_btn, SIGNAL("clicked()"), self.addSizeToList)
    QObject.connect(self.dock.removeSize_btn, SIGNAL("clicked()"), self.removeSizeFromList)
  def addSizeToList(self):
    value = self.dock.insertSize_txtField.text()
    self.sizeListModel.insertRows(value)
  def removeSizeFromList(self):
    selected = self.dock.sizeList.selectedIndexes()
    for selection in selected:
      self.sizeListModel.removeRows(selection)
  def startNetworkValidation(self):
      self.netEnv = NetworkEnvironment()
      self.netEnv.verifyObjectConnections()
  def startHeatlossCalc(self):
    anaHeat = AnalyzeHeatLoss(self.netEnv)
    logging.info('STAGE 1 | Starting heatloss analysis.' \
                  'Calculating network heatloss for the first nodes after taps first.')
    anaHeat.doAnalyze()
    logging.info('STAGE 2 | Analyze network heatlos on next nodes in network.')
    anaHeat.analyzeNextNodes()
  def configureLogging(self):
    """Configures the logging env"""
    logging.basicConfig(filename='/Users/cruizer/Documents/kristofQgis/plugin.log',
                        level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s:%(message)s')
    