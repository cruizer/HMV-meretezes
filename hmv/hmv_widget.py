# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hmv_widget.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_HmvWidget(QtGui.QDockWidget):
    def setupUi(self, HmvWidget):
        HmvWidget.setObjectName(_fromUtf8("HmvWidget"))
        HmvWidget.resize(444, 853)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(HmvWidget.sizePolicy().hasHeightForWidth())
        HmvWidget.setSizePolicy(sizePolicy)
        self.dockWidgetContents = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents.setSizePolicy(sizePolicy)
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tabs_Wdg = QtGui.QTabWidget(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs_Wdg.sizePolicy().hasHeightForWidth())
        self.tabs_Wdg.setSizePolicy(sizePolicy)
        self.tabs_Wdg.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabs_Wdg.setObjectName(_fromUtf8("tabs_Wdg"))
        self.networkVal_tab = QtGui.QWidget()
        self.networkVal_tab.setObjectName(_fromUtf8("networkVal_tab"))
        self.verticalLayout = QtGui.QVBoxLayout(self.networkVal_tab)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.validateStart_btn = QtGui.QPushButton(self.networkVal_tab)
        self.validateStart_btn.setObjectName(_fromUtf8("validateStart_btn"))
        self.verticalLayout.addWidget(self.validateStart_btn)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.checkStatus_label = QtGui.QLabel(self.networkVal_tab)
        self.checkStatus_label.setObjectName(_fromUtf8("checkStatus_label"))
        self.horizontalLayout.addWidget(self.checkStatus_label)
        self.checkStatusValue_label = QtGui.QLabel(self.networkVal_tab)
        self.checkStatusValue_label.setObjectName(_fromUtf8("checkStatusValue_label"))
        self.horizontalLayout.addWidget(self.checkStatusValue_label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.numberOfElements_label = QtGui.QLabel(self.networkVal_tab)
        self.numberOfElements_label.setObjectName(_fromUtf8("numberOfElements_label"))
        self.horizontalLayout_2.addWidget(self.numberOfElements_label)
        self.numberOfElementsValue_label = QtGui.QLabel(self.networkVal_tab)
        self.numberOfElementsValue_label.setObjectName(_fromUtf8("numberOfElementsValue_label"))
        self.horizontalLayout_2.addWidget(self.numberOfElementsValue_label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.numberOfErrElements_label = QtGui.QLabel(self.networkVal_tab)
        self.numberOfErrElements_label.setObjectName(_fromUtf8("numberOfErrElements_label"))
        self.horizontalLayout_3.addWidget(self.numberOfErrElements_label)
        self.numberOfErrElementsValue_label = QtGui.QLabel(self.networkVal_tab)
        self.numberOfErrElementsValue_label.setObjectName(_fromUtf8("numberOfErrElementsValue_label"))
        self.horizontalLayout_3.addWidget(self.numberOfErrElementsValue_label)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.errElementsList_label = QtGui.QLabel(self.networkVal_tab)
        self.errElementsList_label.setObjectName(_fromUtf8("errElementsList_label"))
        self.verticalLayout.addWidget(self.errElementsList_label)
        self.errElements_table = QtGui.QTableView(self.networkVal_tab)
        self.errElements_table.setObjectName(_fromUtf8("errElements_table"))
        self.verticalLayout.addWidget(self.errElements_table)
        self.validateStart_btn.raise_()
        self.numberOfErrElements_label.raise_()
        self.errElementsList_label.raise_()
        self.errElements_table.raise_()
        self.tabs_Wdg.addTab(self.networkVal_tab, _fromUtf8(""))
        self.pipeSize_tab = QtGui.QWidget()
        self.pipeSize_tab.setObjectName(_fromUtf8("pipeSize_tab"))
        self.verticalLayout_15 = QtGui.QVBoxLayout(self.pipeSize_tab)
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.addRemoveButtons = QtGui.QHBoxLayout()
        self.addRemoveButtons.setObjectName(_fromUtf8("addRemoveButtons"))
        self.addSize_btn = QtGui.QPushButton(self.pipeSize_tab)
        self.addSize_btn.setObjectName(_fromUtf8("addSize_btn"))
        self.addRemoveButtons.addWidget(self.addSize_btn)
        self.removeSize_btn = QtGui.QPushButton(self.pipeSize_tab)
        self.removeSize_btn.setObjectName(_fromUtf8("removeSize_btn"))
        self.addRemoveButtons.addWidget(self.removeSize_btn)
        self.label = QtGui.QLabel(self.pipeSize_tab)
        self.label.setObjectName(_fromUtf8("label"))
        self.addRemoveButtons.addWidget(self.label)
        self.insertSize_txtField = QtGui.QLineEdit(self.pipeSize_tab)
        self.insertSize_txtField.setObjectName(_fromUtf8("insertSize_txtField"))
        self.addRemoveButtons.addWidget(self.insertSize_txtField)
        self.verticalLayout_15.addLayout(self.addRemoveButtons)
        self.sizeList = QtGui.QListView(self.pipeSize_tab)
        self.sizeList.setObjectName(_fromUtf8("sizeList"))
        self.verticalLayout_15.addWidget(self.sizeList)
        self.tabs_Wdg.addTab(self.pipeSize_tab, _fromUtf8(""))
        self.analyze_tab = QtGui.QWidget()
        self.analyze_tab.setObjectName(_fromUtf8("analyze_tab"))
        self.label_2 = QtGui.QLabel(self.analyze_tab)
        self.label_2.setGeometry(QtCore.QRect(10, 210, 121, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.analyze_tab)
        self.label_3.setGeometry(QtCore.QRect(10, 310, 261, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.line = QtGui.QFrame(self.analyze_tab)
        self.line.setGeometry(QtCore.QRect(10, 195, 381, 21))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_10 = QtGui.QLabel(self.analyze_tab)
        self.label_10.setGeometry(QtCore.QRect(10, 240, 251, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.layoutWidget = QtGui.QWidget(self.analyze_tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 168))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.theAnalysis_btn = QtGui.QPushButton(self.layoutWidget)
        self.theAnalysis_btn.setObjectName(_fromUtf8("theAnalysis_btn"))
        self.verticalLayout_3.addWidget(self.theAnalysis_btn)
        self.verifyNotification_lbl = QtGui.QLabel(self.layoutWidget)
        self.verifyNotification_lbl.setEnabled(True)
        self.verifyNotification_lbl.setWordWrap(True)
        self.verifyNotification_lbl.setObjectName(_fromUtf8("verifyNotification_lbl"))
        self.verticalLayout_3.addWidget(self.verifyNotification_lbl)
        self.layoutWidget1 = QtGui.QWidget(self.analyze_tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 340, 171, 41))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.circFlow_label = QtGui.QLabel(self.layoutWidget1)
        self.circFlow_label.setObjectName(_fromUtf8("circFlow_label"))
        self.horizontalLayout_8.addWidget(self.circFlow_label)
        self.circFlow_combo = QtGui.QComboBox(self.layoutWidget1)
        self.circFlow_combo.setObjectName(_fromUtf8("circFlow_combo"))
        self.circFlow_combo.addItem(_fromUtf8(""))
        self.circFlow_combo.addItem(_fromUtf8(""))
        self.horizontalLayout_8.addWidget(self.circFlow_combo)
        self.layoutWidget2 = QtGui.QWidget(self.analyze_tab)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 270, 91, 31))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.totalHeatloss_label = QtGui.QLabel(self.layoutWidget2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.totalHeatloss_label.sizePolicy().hasHeightForWidth())
        self.totalHeatloss_label.setSizePolicy(sizePolicy)
        self.totalHeatloss_label.setObjectName(_fromUtf8("totalHeatloss_label"))
        self.horizontalLayout_9.addWidget(self.totalHeatloss_label)
        self.label_12 = QtGui.QLabel(self.layoutWidget2)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_9.addWidget(self.label_12)
        self.verticalLayoutWidget = QtGui.QWidget(self.analyze_tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(90, 500, 296, 100))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.showResults_btn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.showResults_btn.setObjectName(_fromUtf8("showResults_btn"))
        self.verticalLayout_5.addWidget(self.showResults_btn)
        self.showPressureResults_btn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.showPressureResults_btn.setObjectName(_fromUtf8("showPressureResults_btn"))
        self.verticalLayout_5.addWidget(self.showPressureResults_btn)
        self.showPipeFlowChart_btn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.showPipeFlowChart_btn.setObjectName(_fromUtf8("showPipeFlowChart_btn"))
        self.verticalLayout_5.addWidget(self.showPipeFlowChart_btn)
        self.tabs_Wdg.addTab(self.analyze_tab, _fromUtf8(""))
        self.settings_tab = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_tab.sizePolicy().hasHeightForWidth())
        self.settings_tab.setSizePolicy(sizePolicy)
        self.settings_tab.setObjectName(_fromUtf8("settings_tab"))
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.settings_tab)
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.scrollArea = QtGui.QScrollArea(self.settings_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 402, 754))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_14 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.resetSettings_btn = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.resetSettings_btn.setObjectName(_fromUtf8("resetSettings_btn"))
        self.horizontalLayout_4.addWidget(self.resetSettings_btn)
        self.saveSettings_btn = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.saveSettings_btn.setObjectName(_fromUtf8("saveSettings_btn"))
        self.horizontalLayout_4.addWidget(self.saveSettings_btn)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_4)
        self.verticalLayout_14.addLayout(self.horizontalLayout_11)
        self.label_17 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.verticalLayout_14.addWidget(self.label_17)
        self.refreshLayers_btn = QtGui.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refreshLayers_btn.sizePolicy().hasHeightForWidth())
        self.refreshLayers_btn.setSizePolicy(sizePolicy)
        self.refreshLayers_btn.setBaseSize(QtCore.QSize(0, 0))
        self.refreshLayers_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.refreshLayers_btn.setStyleSheet(_fromUtf8("border-image : url(:/refresh/refresh.svg) 0 0 0 0 stretch stretch;"))
        self.refreshLayers_btn.setText(_fromUtf8(""))
        self.refreshLayers_btn.setObjectName(_fromUtf8("refreshLayers_btn"))
        self.verticalLayout_14.addWidget(self.refreshLayers_btn)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.label_15 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.verticalLayout_8.addWidget(self.label_15)
        self.label_16 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.verticalLayout_8.addWidget(self.label_16)
        self.horizontalLayout_6.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.nodeLayerSelect_combo = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.nodeLayerSelect_combo.setObjectName(_fromUtf8("nodeLayerSelect_combo"))
        self.verticalLayout_9.addWidget(self.nodeLayerSelect_combo)
        self.pipeLayerSelect_combo = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.pipeLayerSelect_combo.setObjectName(_fromUtf8("pipeLayerSelect_combo"))
        self.verticalLayout_9.addWidget(self.pipeLayerSelect_combo)
        self.horizontalLayout_6.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.formatLayers_btn = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.formatLayers_btn.setObjectName(_fromUtf8("formatLayers_btn"))
        self.verticalLayout_10.addWidget(self.formatLayers_btn)
        self.horizontalLayout_6.addLayout(self.verticalLayout_10)
        self.verticalLayout_14.addLayout(self.horizontalLayout_6)
        self.line_2 = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_14.addWidget(self.line_2)
        self.label_14 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.verticalLayout_14.addWidget(self.label_14)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_8 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_4.addWidget(self.label_8)
        self.label_6 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_4.addWidget(self.label_6)
        self.label_4 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_4.addWidget(self.label_4)
        self.label_11 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_4.addWidget(self.label_11)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.density_txtField = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.density_txtField.setObjectName(_fromUtf8("density_txtField"))
        self.verticalLayout_6.addWidget(self.density_txtField)
        self.specificHeat_txtField = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.specificHeat_txtField.setObjectName(_fromUtf8("specificHeat_txtField"))
        self.verticalLayout_6.addWidget(self.specificHeat_txtField)
        self.deltaTheta_txtField = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.deltaTheta_txtField.setObjectName(_fromUtf8("deltaTheta_txtField"))
        self.verticalLayout_6.addWidget(self.deltaTheta_txtField)
        self.pipeSpeedLimit_txtField = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.pipeSpeedLimit_txtField.setObjectName(_fromUtf8("pipeSpeedLimit_txtField"))
        self.verticalLayout_6.addWidget(self.pipeSpeedLimit_txtField)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_9 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_7.addWidget(self.label_9)
        self.label_7 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_7.addWidget(self.label_7)
        self.label_5 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_7.addWidget(self.label_5)
        self.label_13 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_7.addWidget(self.label_13)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.verticalLayout_14.addLayout(self.horizontalLayout_5)
        self.line_3 = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_14.addWidget(self.line_3)
        self.label_18 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.verticalLayout_14.addWidget(self.label_18)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.label_19 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.verticalLayout_11.addWidget(self.label_19)
        self.label_20 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.verticalLayout_11.addWidget(self.label_20)
        self.label_23 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.verticalLayout_11.addWidget(self.label_23)
        self.label_21 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.verticalLayout_11.addWidget(self.label_21)
        self.label_22 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.verticalLayout_11.addWidget(self.label_22)
        self.horizontalLayout_7.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.newLayerName_txtField = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.newLayerName_txtField.setObjectName(_fromUtf8("newLayerName_txtField"))
        self.verticalLayout_12.addWidget(self.newLayerName_txtField)
        self.newLayerDbFile_txtField = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.newLayerDbFile_txtField.setObjectName(_fromUtf8("newLayerDbFile_txtField"))
        self.verticalLayout_12.addWidget(self.newLayerDbFile_txtField)
        self.autoDbFileName_checkbox = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.autoDbFileName_checkbox.setText(_fromUtf8(""))
        self.autoDbFileName_checkbox.setChecked(True)
        self.autoDbFileName_checkbox.setObjectName(_fromUtf8("autoDbFileName_checkbox"))
        self.verticalLayout_12.addWidget(self.autoDbFileName_checkbox)
        self.newLayerType_combo = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.newLayerType_combo.setObjectName(_fromUtf8("newLayerType_combo"))
        self.newLayerType_combo.addItem(_fromUtf8(""))
        self.newLayerType_combo.addItem(_fromUtf8(""))
        self.verticalLayout_12.addWidget(self.newLayerType_combo)
        self.newLayerAddToRegistry_checkbox = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.newLayerAddToRegistry_checkbox.setText(_fromUtf8(""))
        self.newLayerAddToRegistry_checkbox.setChecked(True)
        self.newLayerAddToRegistry_checkbox.setObjectName(_fromUtf8("newLayerAddToRegistry_checkbox"))
        self.verticalLayout_12.addWidget(self.newLayerAddToRegistry_checkbox)
        self.horizontalLayout_7.addLayout(self.verticalLayout_12)
        self.verticalLayout_14.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_24 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.horizontalLayout_10.addWidget(self.label_24)
        self.layerWorkingDirectory_txtField = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.layerWorkingDirectory_txtField.setObjectName(_fromUtf8("layerWorkingDirectory_txtField"))
        self.horizontalLayout_10.addWidget(self.layerWorkingDirectory_txtField)
        self.verticalLayout_14.addLayout(self.horizontalLayout_10)
        self.createNewLayer_btn = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.createNewLayer_btn.setObjectName(_fromUtf8("createNewLayer_btn"))
        self.verticalLayout_14.addWidget(self.createNewLayer_btn)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_13.addWidget(self.scrollArea)
        self.tabs_Wdg.addTab(self.settings_tab, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabs_Wdg)
        HmvWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(HmvWidget)
        self.tabs_Wdg.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(HmvWidget)

    def retranslateUi(self, HmvWidget):
        HmvWidget.setWindowTitle(_translate("HmvWidget", "HMV Meretezes", None))
        self.validateStart_btn.setText(_translate("HmvWidget", "Hálózat ellenőrzés", None))
        self.checkStatus_label.setText(_translate("HmvWidget", "Státusz:", None))
        self.checkStatusValue_label.setText(_translate("HmvWidget", "Nem Ellenőrzött", None))
        self.numberOfElements_label.setText(_translate("HmvWidget", "Összes elem száma:", None))
        self.numberOfElementsValue_label.setText(_translate("HmvWidget", "0", None))
        self.numberOfErrElements_label.setText(_translate("HmvWidget", "Hibás elemek száma:", None))
        self.numberOfErrElementsValue_label.setText(_translate("HmvWidget", "0", None))
        self.errElementsList_label.setText(_translate("HmvWidget", "Hibás elemek (csatlakozás nem megfelelő)", None))
        self.tabs_Wdg.setTabText(self.tabs_Wdg.indexOf(self.networkVal_tab), _translate("HmvWidget", "Hálózat ell.", None))
        self.addSize_btn.setText(_translate("HmvWidget", "+", None))
        self.removeSize_btn.setText(_translate("HmvWidget", "-", None))
        self.label.setText(_translate("HmvWidget", "Méret hozzáadása:", None))
        self.tabs_Wdg.setTabText(self.tabs_Wdg.indexOf(self.pipeSize_tab), _translate("HmvWidget", "Cső méretek", None))
        self.label_2.setText(_translate("HmvWidget", "Részeredmények", None))
        self.label_3.setText(_translate("HmvWidget", "Szivattyú által biztosítandó téfogatáram", None))
        self.label_10.setText(_translate("HmvWidget", "Teljes előremenő hálózat hővesztesége", None))
        self.theAnalysis_btn.setText(_translate("HmvWidget", "Analízis", None))
        self.verifyNotification_lbl.setText(_translate("HmvWidget", "<html><head/><body><p><span style=\" color:#e82517;\">Hálózat ellenőrzés szükséges! Még nem történt hálózat ellenőrzés, vagy a hálózat megváltozott.</span></p></body></html>", None))
        self.circFlow_label.setText(_translate("HmvWidget", "-", None))
        self.circFlow_combo.setItemText(0, _translate("HmvWidget", "dm3/h", None))
        self.circFlow_combo.setItemText(1, _translate("HmvWidget", "m3/sec", None))
        self.totalHeatloss_label.setText(_translate("HmvWidget", "-", None))
        self.label_12.setText(_translate("HmvWidget", "W", None))
        self.showResults_btn.setText(_translate("HmvWidget", "Eredmények mutatása", None))
        self.showPressureResults_btn.setText(_translate("HmvWidget", "Körönkénti nyomás / fojtás eredmények", None))
        self.showPipeFlowChart_btn.setText(_translate("HmvWidget", "Áramlás eredmények", None))
        self.tabs_Wdg.setTabText(self.tabs_Wdg.indexOf(self.analyze_tab), _translate("HmvWidget", "Analízis", None))
        self.resetSettings_btn.setText(_translate("HmvWidget", "Visszaállítás", None))
        self.saveSettings_btn.setText(_translate("HmvWidget", "Mentés", None))
        self.label_17.setText(_translate("HmvWidget", "Réteg választás", None))
        self.label_15.setText(_translate("HmvWidget", "Elemek QGIS réteg:", None))
        self.label_16.setText(_translate("HmvWidget", "Csőhálózat QGIS réteg:", None))
        self.formatLayers_btn.setText(_translate("HmvWidget", "Formázás", None))
        self.label_14.setText(_translate("HmvWidget", "Kiindulási adatok", None))
        self.label_8.setText(_translate("HmvWidget", "Sűrűség", None))
        self.label_6.setText(_translate("HmvWidget", "Fajhő", None))
        self.label_4.setText(_translate("HmvWidget", "Δϑ", None))
        self.label_11.setText(_translate("HmvWidget", "Csősebesség", None))
        self.label_9.setText(_translate("HmvWidget", "kg/m3", None))
        self.label_7.setText(_translate("HmvWidget", "J/kgK", None))
        self.label_5.setText(_translate("HmvWidget", "K", None))
        self.label_13.setText(_translate("HmvWidget", "m/s", None))
        self.label_18.setText(_translate("HmvWidget", "Új HMV réteg", None))
        self.label_19.setText(_translate("HmvWidget", "Réteg név", None))
        self.label_20.setText(_translate("HmvWidget", "Adatbázis file név", None))
        self.label_23.setText(_translate("HmvWidget", "File név réteg név szerint?", None))
        self.label_21.setText(_translate("HmvWidget", "Réteg típus", None))
        self.label_22.setText(_translate("HmvWidget", "Hozzáadás a réteg listához?", None))
        self.newLayerType_combo.setItemText(0, _translate("HmvWidget", "szakaszok", None))
        self.newLayerType_combo.setItemText(1, _translate("HmvWidget", "elemek", None))
        self.label_24.setText(_translate("HmvWidget", "Réteg munkakönyvtár", None))
        self.createNewLayer_btn.setText(_translate("HmvWidget", "Létrehoz", None))
        self.tabs_Wdg.setTabText(self.tabs_Wdg.indexOf(self.settings_tab), _translate("HmvWidget", "Beállítások", None))

import refresh_rc
