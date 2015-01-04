# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hmv_widget.ui'
#
# Created: Sun Jan  4 13:14:01 2015
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
        HmvWidget.resize(420, 681)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.sizeListBlock = QtGui.QVBoxLayout()
        self.sizeListBlock.setObjectName(_fromUtf8("sizeListBlock"))
        self.addRemoveButtons = QtGui.QHBoxLayout()
        self.addRemoveButtons.setObjectName(_fromUtf8("addRemoveButtons"))
        self.addSize_btn = QtGui.QPushButton(self.dockWidgetContents)
        self.addSize_btn.setObjectName(_fromUtf8("addSize_btn"))
        self.addRemoveButtons.addWidget(self.addSize_btn)
        self.removeSize_btn = QtGui.QPushButton(self.dockWidgetContents)
        self.removeSize_btn.setObjectName(_fromUtf8("removeSize_btn"))
        self.addRemoveButtons.addWidget(self.removeSize_btn)
        self.label = QtGui.QLabel(self.dockWidgetContents)
        self.label.setObjectName(_fromUtf8("label"))
        self.addRemoveButtons.addWidget(self.label)
        self.insertSize_txtField = QtGui.QLineEdit(self.dockWidgetContents)
        self.insertSize_txtField.setObjectName(_fromUtf8("insertSize_txtField"))
        self.addRemoveButtons.addWidget(self.insertSize_txtField)
        self.sizeListBlock.addLayout(self.addRemoveButtons)
        self.sizeList = QtGui.QListView(self.dockWidgetContents)
        self.sizeList.setObjectName(_fromUtf8("sizeList"))
        self.sizeListBlock.addWidget(self.sizeList)
        self.verticalLayout.addLayout(self.sizeListBlock)
        self.validateStart_btn = QtGui.QPushButton(self.dockWidgetContents)
        self.validateStart_btn.setObjectName(_fromUtf8("validateStart_btn"))
        self.verticalLayout.addWidget(self.validateStart_btn)
        self.heatlossStart_btn = QtGui.QPushButton(self.dockWidgetContents)
        self.heatlossStart_btn.setObjectName(_fromUtf8("heatlossStart_btn"))
        self.verticalLayout.addWidget(self.heatlossStart_btn)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        HmvWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(HmvWidget)
        QtCore.QMetaObject.connectSlotsByName(HmvWidget)

    def retranslateUi(self, HmvWidget):
        HmvWidget.setWindowTitle(_translate("HmvWidget", "HMV Meretezes", None))
        self.addSize_btn.setText(_translate("HmvWidget", "+", None))
        self.removeSize_btn.setText(_translate("HmvWidget", "-", None))
        self.label.setText(_translate("HmvWidget", "Méret hozzáadása:", None))
        self.validateStart_btn.setText(_translate("HmvWidget", "Hálózat ellenőrzés", None))
        self.heatlossStart_btn.setText(_translate("HmvWidget", "Hőveszteség mérés", None))

