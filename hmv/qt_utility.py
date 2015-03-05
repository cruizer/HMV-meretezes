from PyQt4 import QtGui

# This is to properly encode GUI test label data
try:
  _encoding = QtGui.QApplication.UnicodeUTF8 # pylint: disable=E1101
  def QtTranslate(context, text, disambig):
    return QtGui.QApplication.translate(context, text, disambig, _encoding) # pylint: disable=E1101
except AttributeError:
  def QtTranslate(context, text, disambig):
    return QtGui.QApplication.translate(context, text, disambig) # pylint: disable=E1101
    