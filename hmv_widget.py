# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hmv_widget.ui'
#
# Created: Mon Nov 17 22:48:17 2014
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
        HmvWidget.resize(400, 300)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.heatlossStart_btn = QtGui.QPushButton(self.dockWidgetContents)
        self.heatlossStart_btn.setObjectName(_fromUtf8("heatlossStart_btn"))
        self.verticalLayout.addWidget(self.heatlossStart_btn)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        HmvWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(HmvWidget)
        QtCore.QMetaObject.connectSlotsByName(HmvWidget)

    def retranslateUi(self, HmvWidget):
        HmvWidget.setWindowTitle(_translate("HmvWidget", "HMV Meretezes", None))
        self.heatlossStart_btn.setText(_translate("HmvWidget", "Hoveszteseg meres", None))

