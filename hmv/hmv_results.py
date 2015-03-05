# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hmv_results.ui'
#
# Created: Sat Jan 17 14:01:43 2015
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

class Ui_result_widget(QtGui.QWidget):
    def setupUi(self, result_widget):
        result_widget.setObjectName(_fromUtf8("result_widget"))
        result_widget.resize(1303, 753)
        self.results_table = QtGui.QTableView(result_widget)
        self.results_table.setGeometry(QtCore.QRect(40, 30, 1231, 661))
        self.results_table.setObjectName(_fromUtf8("results_table"))
        self.closeWindow_btn = QtGui.QPushButton(result_widget)
        self.closeWindow_btn.setGeometry(QtCore.QRect(1140, 710, 114, 32))
        self.closeWindow_btn.setObjectName(_fromUtf8("closeWindow_btn"))

        self.retranslateUi(result_widget)
        QtCore.QMetaObject.connectSlotsByName(result_widget)

    def retranslateUi(self, result_widget):
        result_widget.setWindowTitle(_translate("result_widget", "Eredmények", None))
        self.closeWindow_btn.setText(_translate("result_widget", "Close", None))

