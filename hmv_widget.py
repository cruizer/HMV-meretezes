# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hmv_widget.ui'
#
# Created: Mon Jan 12 19:44:37 2015
#      by: PyQt4 UI code generator 4.10.3
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
        HmvWidget.resize(428, 681)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tabs_Wdg = QtGui.QTabWidget(self.dockWidgetContents)
        self.tabs_Wdg.setObjectName(_fromUtf8("tabs_Wdg"))
        self.networkVal_tab = QtGui.QWidget()
        self.networkVal_tab.setObjectName(_fromUtf8("networkVal_tab"))
        self.widget = QtGui.QWidget(self.networkVal_tab)
        self.widget.setGeometry(QtCore.QRect(0, 10, 341, 491))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.validateStart_btn = QtGui.QPushButton(self.widget)
        self.validateStart_btn.setObjectName(_fromUtf8("validateStart_btn"))
        self.verticalLayout.addWidget(self.validateStart_btn)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.checkStatus_label = QtGui.QLabel(self.widget)
        self.checkStatus_label.setObjectName(_fromUtf8("checkStatus_label"))
        self.horizontalLayout.addWidget(self.checkStatus_label)
        self.checkStatusValue_label = QtGui.QLabel(self.widget)
        self.checkStatusValue_label.setObjectName(_fromUtf8("checkStatusValue_label"))
        self.horizontalLayout.addWidget(self.checkStatusValue_label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.numberOfElements_label = QtGui.QLabel(self.widget)
        self.numberOfElements_label.setObjectName(_fromUtf8("numberOfElements_label"))
        self.horizontalLayout_2.addWidget(self.numberOfElements_label)
        self.numberOfElementsValue_label = QtGui.QLabel(self.widget)
        self.numberOfElementsValue_label.setObjectName(_fromUtf8("numberOfElementsValue_label"))
        self.horizontalLayout_2.addWidget(self.numberOfElementsValue_label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.numberOfErrElements_label = QtGui.QLabel(self.widget)
        self.numberOfErrElements_label.setObjectName(_fromUtf8("numberOfErrElements_label"))
        self.horizontalLayout_3.addWidget(self.numberOfErrElements_label)
        self.numberOfErrElementsValue_label = QtGui.QLabel(self.widget)
        self.numberOfErrElementsValue_label.setObjectName(_fromUtf8("numberOfErrElementsValue_label"))
        self.horizontalLayout_3.addWidget(self.numberOfErrElementsValue_label)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.errElementsList_label = QtGui.QLabel(self.widget)
        self.errElementsList_label.setObjectName(_fromUtf8("errElementsList_label"))
        self.verticalLayout.addWidget(self.errElementsList_label)
        self.errElements_table = QtGui.QTableView(self.widget)
        self.errElements_table.setObjectName(_fromUtf8("errElements_table"))
        self.verticalLayout.addWidget(self.errElements_table)
        self.tabs_Wdg.addTab(self.networkVal_tab, _fromUtf8(""))
        self.pipeSize_tab = QtGui.QWidget()
        self.pipeSize_tab.setObjectName(_fromUtf8("pipeSize_tab"))
        self.widget1 = QtGui.QWidget(self.pipeSize_tab)
        self.widget1.setGeometry(QtCore.QRect(0, 0, 331, 501))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.sizeListBlock = QtGui.QVBoxLayout(self.widget1)
        self.sizeListBlock.setMargin(0)
        self.sizeListBlock.setObjectName(_fromUtf8("sizeListBlock"))
        self.addRemoveButtons = QtGui.QHBoxLayout()
        self.addRemoveButtons.setObjectName(_fromUtf8("addRemoveButtons"))
        self.addSize_btn = QtGui.QPushButton(self.widget1)
        self.addSize_btn.setObjectName(_fromUtf8("addSize_btn"))
        self.addRemoveButtons.addWidget(self.addSize_btn)
        self.removeSize_btn = QtGui.QPushButton(self.widget1)
        self.removeSize_btn.setObjectName(_fromUtf8("removeSize_btn"))
        self.addRemoveButtons.addWidget(self.removeSize_btn)
        self.label = QtGui.QLabel(self.widget1)
        self.label.setObjectName(_fromUtf8("label"))
        self.addRemoveButtons.addWidget(self.label)
        self.insertSize_txtField = QtGui.QLineEdit(self.widget1)
        self.insertSize_txtField.setObjectName(_fromUtf8("insertSize_txtField"))
        self.addRemoveButtons.addWidget(self.insertSize_txtField)
        self.sizeListBlock.addLayout(self.addRemoveButtons)
        self.sizeList = QtGui.QListView(self.widget1)
        self.sizeList.setObjectName(_fromUtf8("sizeList"))
        self.sizeListBlock.addWidget(self.sizeList)
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
        self.widget2 = QtGui.QWidget(self.analyze_tab)
        self.widget2.setGeometry(QtCore.QRect(0, 10, 261, 168))
        self.widget2.setObjectName(_fromUtf8("widget2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget2)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.heatlossStart_btn = QtGui.QPushButton(self.widget2)
        self.heatlossStart_btn.setObjectName(_fromUtf8("heatlossStart_btn"))
        self.verticalLayout_3.addWidget(self.heatlossStart_btn)
        self.flowRateStart_btn = QtGui.QPushButton(self.widget2)
        self.flowRateStart_btn.setObjectName(_fromUtf8("flowRateStart_btn"))
        self.verticalLayout_3.addWidget(self.flowRateStart_btn)
        self.returnPipeDiaStart_btn = QtGui.QPushButton(self.widget2)
        self.returnPipeDiaStart_btn.setObjectName(_fromUtf8("returnPipeDiaStart_btn"))
        self.verticalLayout_3.addWidget(self.returnPipeDiaStart_btn)
        self.pipeDragStart_btn = QtGui.QPushButton(self.widget2)
        self.pipeDragStart_btn.setObjectName(_fromUtf8("pipeDragStart_btn"))
        self.verticalLayout_3.addWidget(self.pipeDragStart_btn)
        self.presurreLossStart_btn = QtGui.QPushButton(self.widget2)
        self.presurreLossStart_btn.setObjectName(_fromUtf8("presurreLossStart_btn"))
        self.verticalLayout_3.addWidget(self.presurreLossStart_btn)
        self.widget3 = QtGui.QWidget(self.analyze_tab)
        self.widget3.setGeometry(QtCore.QRect(10, 340, 171, 26))
        self.widget3.setObjectName(_fromUtf8("widget3"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.widget3)
        self.horizontalLayout_8.setMargin(0)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.circFlow_label = QtGui.QLabel(self.widget3)
        self.circFlow_label.setObjectName(_fromUtf8("circFlow_label"))
        self.horizontalLayout_8.addWidget(self.circFlow_label)
        self.circFlow_combo = QtGui.QComboBox(self.widget3)
        self.circFlow_combo.setObjectName(_fromUtf8("circFlow_combo"))
        self.circFlow_combo.addItem(_fromUtf8(""))
        self.circFlow_combo.addItem(_fromUtf8(""))
        self.horizontalLayout_8.addWidget(self.circFlow_combo)
        self.widget4 = QtGui.QWidget(self.analyze_tab)
        self.widget4.setGeometry(QtCore.QRect(10, 270, 91, 18))
        self.widget4.setObjectName(_fromUtf8("widget4"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.widget4)
        self.horizontalLayout_9.setMargin(0)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.totalHeatloss_label = QtGui.QLabel(self.widget4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.totalHeatloss_label.sizePolicy().hasHeightForWidth())
        self.totalHeatloss_label.setSizePolicy(sizePolicy)
        self.totalHeatloss_label.setObjectName(_fromUtf8("totalHeatloss_label"))
        self.horizontalLayout_9.addWidget(self.totalHeatloss_label)
        self.label_12 = QtGui.QLabel(self.widget4)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_9.addWidget(self.label_12)
        self.tabs_Wdg.addTab(self.analyze_tab, _fromUtf8(""))
        self.settings_tab = QtGui.QWidget()
        self.settings_tab.setObjectName(_fromUtf8("settings_tab"))
        self.widget5 = QtGui.QWidget(self.settings_tab)
        self.widget5.setGeometry(QtCore.QRect(10, 40, 345, 91))
        self.widget5.setObjectName(_fromUtf8("widget5"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.widget5)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_8 = QtGui.QLabel(self.widget5)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_7.addWidget(self.label_8)
        self.density_txtField = QtGui.QLineEdit(self.widget5)
        self.density_txtField.setObjectName(_fromUtf8("density_txtField"))
        self.horizontalLayout_7.addWidget(self.density_txtField)
        self.label_9 = QtGui.QLabel(self.widget5)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_7.addWidget(self.label_9)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_6 = QtGui.QLabel(self.widget5)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_6.addWidget(self.label_6)
        self.specificHeat_txtField = QtGui.QLineEdit(self.widget5)
        self.specificHeat_txtField.setObjectName(_fromUtf8("specificHeat_txtField"))
        self.horizontalLayout_6.addWidget(self.specificHeat_txtField)
        self.label_7 = QtGui.QLabel(self.widget5)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_6.addWidget(self.label_7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_4 = QtGui.QLabel(self.widget5)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_5.addWidget(self.label_4)
        self.deltaTheta_txtField = QtGui.QLineEdit(self.widget5)
        self.deltaTheta_txtField.setObjectName(_fromUtf8("deltaTheta_txtField"))
        self.horizontalLayout_5.addWidget(self.deltaTheta_txtField)
        self.label_5 = QtGui.QLabel(self.widget5)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.widget6 = QtGui.QWidget(self.settings_tab)
        self.widget6.setGeometry(QtCore.QRect(170, 0, 210, 32))
        self.widget6.setObjectName(_fromUtf8("widget6"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget6)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.resetSettings_btn = QtGui.QPushButton(self.widget6)
        self.resetSettings_btn.setObjectName(_fromUtf8("resetSettings_btn"))
        self.horizontalLayout_4.addWidget(self.resetSettings_btn)
        self.saveSettings_btn = QtGui.QPushButton(self.widget6)
        self.saveSettings_btn.setObjectName(_fromUtf8("saveSettings_btn"))
        self.horizontalLayout_4.addWidget(self.saveSettings_btn)
        self.tabs_Wdg.addTab(self.settings_tab, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabs_Wdg)
        HmvWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(HmvWidget)
        self.tabs_Wdg.setCurrentIndex(2)
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
        self.heatlossStart_btn.setText(_translate("HmvWidget", "Hőveszteség mérés", None))
        self.flowRateStart_btn.setText(_translate("HmvWidget", "Térfogatáram számítás", None))
        self.returnPipeDiaStart_btn.setText(_translate("HmvWidget", "Visszatérő ági csőátmérő számítás", None))
        self.pipeDragStart_btn.setText(_translate("HmvWidget", "Csősúrlódási tényező számítás", None))
        self.presurreLossStart_btn.setText(_translate("HmvWidget", "Kör nyomásesés számítása", None))
        self.circFlow_label.setText(_translate("HmvWidget", "-", None))
        self.circFlow_combo.setItemText(0, _translate("HmvWidget", "dm3/h", None))
        self.circFlow_combo.setItemText(1, _translate("HmvWidget", "m3/sec", None))
        self.totalHeatloss_label.setText(_translate("HmvWidget", "-", None))
        self.label_12.setText(_translate("HmvWidget", "W", None))
        self.tabs_Wdg.setTabText(self.tabs_Wdg.indexOf(self.analyze_tab), _translate("HmvWidget", "Analízis", None))
        self.label_8.setText(_translate("HmvWidget", "Sűrűség", None))
        self.label_9.setText(_translate("HmvWidget", "kg/m3", None))
        self.label_6.setText(_translate("HmvWidget", "Fajhő", None))
        self.label_7.setText(_translate("HmvWidget", "J/kgK", None))
        self.label_4.setText(_translate("HmvWidget", "Δϑ", None))
        self.label_5.setText(_translate("HmvWidget", "K", None))
        self.resetSettings_btn.setText(_translate("HmvWidget", "Visszaállítás", None))
        self.saveSettings_btn.setText(_translate("HmvWidget", "Mentés", None))
        self.tabs_Wdg.setTabText(self.tabs_Wdg.indexOf(self.settings_tab), _translate("HmvWidget", "Beállítások", None))

