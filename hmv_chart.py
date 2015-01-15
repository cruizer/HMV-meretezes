# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hmv_chart.ui'
#
# Created: Wed Jan 14 22:13:57 2015
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

class Ui_pipeFlowChart_wdg(QtGui.QWidget):
    def setupUi(self, pipeFlowChart_wdg):
        pipeFlowChart_wdg.setObjectName(_fromUtf8("pipeFlowChart_wdg"))
        pipeFlowChart_wdg.resize(804, 637)
        self.verticalLayoutWidget = QtGui.QWidget(pipeFlowChart_wdg)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 9, 771, 611))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.chartTarget_lo = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.chartTarget_lo.setMargin(0)
        self.chartTarget_lo.setObjectName(_fromUtf8("chartTarget_lo"))

        self.retranslateUi(pipeFlowChart_wdg)
        QtCore.QMetaObject.connectSlotsByName(pipeFlowChart_wdg)

    def retranslateUi(self, pipeFlowChart_wdg):
        pipeFlowChart_wdg.setWindowTitle(_translate("pipeFlowChart_wdg", "Áramlás", None))

