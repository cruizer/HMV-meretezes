# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hmv_widget.ui'
#
# Created: Sun Jan  4 15:44:09 2015
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
        HmvWidget.resize(429, 681)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.dockWidgetContents)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.networkVal_tab = QtGui.QWidget()
        self.networkVal_tab.setObjectName(_fromUtf8("networkVal_tab"))
        self.validateStart_btn = QtGui.QPushButton(self.networkVal_tab)
        self.validateStart_btn.setGeometry(QtCore.QRect(0, 10, 396, 32))
        self.validateStart_btn.setObjectName(_fromUtf8("validateStart_btn"))
        self.errElementsList_label = QtGui.QLabel(self.networkVal_tab)
        self.errElementsList_label.setGeometry(QtCore.QRect(10, 160, 101, 16))
        self.errElementsList_label.setObjectName(_fromUtf8("errElementsList_label"))
        self.errElements_table = QtGui.QTableView(self.networkVal_tab)
        self.errElements_table.setGeometry(QtCore.QRect(10, 190, 256, 192))
        self.errElements_table.setObjectName(_fromUtf8("errElements_table"))
        self.widget = QtGui.QWidget(self.networkVal_tab)
        self.widget.setGeometry(QtCore.QRect(10, 70, 321, 18))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.checkStatus_label = QtGui.QLabel(self.widget)
        self.checkStatus_label.setObjectName(_fromUtf8("checkStatus_label"))
        self.horizontalLayout.addWidget(self.checkStatus_label)
        self.checkStatusValue_label = QtGui.QLabel(self.widget)
        self.checkStatusValue_label.setObjectName(_fromUtf8("checkStatusValue_label"))
        self.horizontalLayout.addWidget(self.checkStatusValue_label)
        self.widget1 = QtGui.QWidget(self.networkVal_tab)
        self.widget1.setGeometry(QtCore.QRect(10, 90, 321, 18))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.numberOfElements_label = QtGui.QLabel(self.widget1)
        self.numberOfElements_label.setObjectName(_fromUtf8("numberOfElements_label"))
        self.horizontalLayout_2.addWidget(self.numberOfElements_label)
        self.numberOfElementsValue_label = QtGui.QLabel(self.widget1)
        self.numberOfElementsValue_label.setObjectName(_fromUtf8("numberOfElementsValue_label"))
        self.horizontalLayout_2.addWidget(self.numberOfElementsValue_label)
        self.widget2 = QtGui.QWidget(self.networkVal_tab)
        self.widget2.setGeometry(QtCore.QRect(10, 110, 321, 18))
        self.widget2.setObjectName(_fromUtf8("widget2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.numberOfErrElements_label = QtGui.QLabel(self.widget2)
        self.numberOfErrElements_label.setObjectName(_fromUtf8("numberOfErrElements_label"))
        self.horizontalLayout_3.addWidget(self.numberOfErrElements_label)
        self.numberOfErrElementsValue_label = QtGui.QLabel(self.widget2)
        self.numberOfErrElementsValue_label.setObjectName(_fromUtf8("numberOfErrElementsValue_label"))
        self.horizontalLayout_3.addWidget(self.numberOfErrElementsValue_label)
        self.tabWidget.addTab(self.networkVal_tab, _fromUtf8(""))
        self.pipeSize_tab = QtGui.QWidget()
        self.pipeSize_tab.setObjectName(_fromUtf8("pipeSize_tab"))
        self.widget3 = QtGui.QWidget(self.pipeSize_tab)
        self.widget3.setGeometry(QtCore.QRect(0, 0, 394, 501))
        self.widget3.setObjectName(_fromUtf8("widget3"))
        self.sizeListBlock = QtGui.QVBoxLayout(self.widget3)
        self.sizeListBlock.setMargin(0)
        self.sizeListBlock.setObjectName(_fromUtf8("sizeListBlock"))
        self.addRemoveButtons = QtGui.QHBoxLayout()
        self.addRemoveButtons.setObjectName(_fromUtf8("addRemoveButtons"))
        self.addSize_btn = QtGui.QPushButton(self.widget3)
        self.addSize_btn.setObjectName(_fromUtf8("addSize_btn"))
        self.addRemoveButtons.addWidget(self.addSize_btn)
        self.removeSize_btn = QtGui.QPushButton(self.widget3)
        self.removeSize_btn.setObjectName(_fromUtf8("removeSize_btn"))
        self.addRemoveButtons.addWidget(self.removeSize_btn)
        self.label = QtGui.QLabel(self.widget3)
        self.label.setObjectName(_fromUtf8("label"))
        self.addRemoveButtons.addWidget(self.label)
        self.insertSize_txtField = QtGui.QLineEdit(self.widget3)
        self.insertSize_txtField.setObjectName(_fromUtf8("insertSize_txtField"))
        self.addRemoveButtons.addWidget(self.insertSize_txtField)
        self.sizeListBlock.addLayout(self.addRemoveButtons)
        self.sizeList = QtGui.QListView(self.widget3)
        self.sizeList.setObjectName(_fromUtf8("sizeList"))
        self.sizeListBlock.addWidget(self.sizeList)
        self.tabWidget.addTab(self.pipeSize_tab, _fromUtf8(""))
        self.analyze_tab = QtGui.QWidget()
        self.analyze_tab.setObjectName(_fromUtf8("analyze_tab"))
        self.heatlossStart_btn = QtGui.QPushButton(self.analyze_tab)
        self.heatlossStart_btn.setGeometry(QtCore.QRect(0, 10, 417, 32))
        self.heatlossStart_btn.setObjectName(_fromUtf8("heatlossStart_btn"))
        self.tabWidget.addTab(self.analyze_tab, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget)
        HmvWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(HmvWidget)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(HmvWidget)

    def retranslateUi(self, HmvWidget):
        HmvWidget.setWindowTitle(_translate("HmvWidget", "HMV Meretezes", None))
        self.validateStart_btn.setText(_translate("HmvWidget", "Hálózat ellenőrzés", None))
        self.errElementsList_label.setText(_translate("HmvWidget", "Hibás elemek", None))
        self.checkStatus_label.setText(_translate("HmvWidget", "Státusz:", None))
        self.checkStatusValue_label.setText(_translate("HmvWidget", "Nem Ellenőrzött", None))
        self.numberOfElements_label.setText(_translate("HmvWidget", "Összes elem száma:", None))
        self.numberOfElementsValue_label.setText(_translate("HmvWidget", "0", None))
        self.numberOfErrElements_label.setText(_translate("HmvWidget", "Hibás elemek száma:", None))
        self.numberOfErrElementsValue_label.setText(_translate("HmvWidget", "0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.networkVal_tab), _translate("HmvWidget", "Hálózat ell.", None))
        self.addSize_btn.setText(_translate("HmvWidget", "+", None))
        self.removeSize_btn.setText(_translate("HmvWidget", "-", None))
        self.label.setText(_translate("HmvWidget", "Méret hozzáadása:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pipeSize_tab), _translate("HmvWidget", "Csőméretek", None))
        self.heatlossStart_btn.setText(_translate("HmvWidget", "Hőveszteség mérés", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.analyze_tab), _translate("HmvWidget", "Analízis", None))

