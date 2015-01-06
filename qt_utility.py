from PyQt4 import QtGui

# This is to properly encode GUI test label data
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def QtTranslate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def QtTranslate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)