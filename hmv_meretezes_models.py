# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
import logging
from qt_utility import QtTranslate

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

class ElementErrorTableModel(QAbstractTableModel):
  """Model used for the list of pipe sizes"""
  def __init__(self, errElements=[['','','']], parent=None):
    super(ElementErrorTableModel, self).__init__()
    self.errElements = errElements
  def rowCount(self, parent=None):
    return len(self.errElements)
  def columnCount(self, parent=None):
    return len(self.errElements[0])
  def data(self, index, role=Qt.DisplayRole):
    if role == Qt.DisplayRole:
      return self.errElements[index.row()][index.column()]
  def insertRows(self, data, parent=QModelIndex()):
    count = len(data)
    self.beginInsertRows(parent, 0, count - 1)
    for element in data:
      self.errElements.append(element)
    logging.info(self.errElements)
    self.endInsertRows()
  def removeRows(self, parent=QModelIndex()):
    self.beginRemoveRows(parent, 0, len(self.errElements) - 1)
    del self.errElements[:]
    self.endRemoveRows()
  def headerData(self, section, orientation=Qt.Horizontal, role=Qt.DisplayRole):
    sectionList = [QtTranslate('HmvWidget', 'QGIS réteg', None), QtTranslate('HmvWidget', 'id', None), QtTranslate('HmvWidget', 'Típus', None)]
    if role == Qt.DisplayRole and orientation == Qt.Horizontal:
      return sectionList[section]