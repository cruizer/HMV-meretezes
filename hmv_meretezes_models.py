from PyQt4.QtCore import *

class SizeListModel(QAbstractListModel):
  """Model used for the list of pipe sizes"""
  def __init__(self, sizes, parent=None):
    super(SizeListModel, self).__init__()
    self.sizes = sizes
  def rowCount(self, parent=None):
    return len(self.sizes)
  def data(self, index, role=Qt.DisplayRole):
    if role == Qt.DisplayRole:
      return self.sizes[index.row()]
  def insertRows(self, data, parent=QModelIndex()):
    for i in xrange(len(self.sizes)):
      if self.sizes[i] > float(data):
        row = i
        break
      elif i == len(self.sizes) - 1:
        row = len(self.sizes)
    self.beginInsertRows(parent, row, row)
    self.sizes.insert(row, float(data))
    self.endInsertRows()
  def removeRows(self, index, parent=QModelIndex()):
    self.beginRemoveRows(parent, index.row(), index.row())
    del self.sizes[index.row()]
    self.endRemoveRows()
