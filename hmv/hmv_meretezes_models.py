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
        sectionList = [QtTranslate('HmvWidget', 'QGIS réteg', None),
                        QtTranslate('HmvWidget', 'id', None),
                        QtTranslate('HmvWidget', 'Típus', None)]
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return sectionList[section]

class ResultsTableModel(QAbstractTableModel):
    """Model used to display sata in the results window"""
    def __init__(self, resultsMatrix, parent=None):
        super(ResultsTableModel, self).__init__()
        # It is a 2D array of the table contents
        self.resultsMatrix = resultsMatrix
    def rowCount(self, parent=None):
        return len(self.resultsMatrix)
    def columnCount(self, parent=None):
        return len(self.resultsMatrix[0])
    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return self.resultsMatrix[index.row()][index.column()]
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignRight
    def headerData(self, section, orientation=Qt.Horizontal, role=Qt.DisplayRole):
        sectionList = [ QtTranslate('result_widget', 'id', None),
                        QtTranslate('result_widget', 'Dm (mm)', None),
                        QtTranslate('result_widget', 'δm (mm)', None),
                        QtTranslate('result_widget', 'km (W/mK)', None),
                        QtTranslate('result_widget', 'qm (W/m)', None),
                        QtTranslate('result_widget', 'Qm (W)', None),
                        QtTranslate('result_widget', 'Vm (l/h)', None),
                        QtTranslate('result_widget', 'wm (m6S)', None),
                        QtTranslate('result_widget', 'Rem', None),
                        QtTranslate('result_widget', 'λm', None),
                        QtTranslate('result_widget', 's\'m (Pa/m)', None),
                        QtTranslate('result_widget', 'dpm (Pa)', None)]
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return sectionList[section]

class PressureTableModel(QAbstractTableModel):
    """Model used to display data in the pressure results window"""
    def __init__(self, pressureMatrix, parent=None):
        super(PressureTableModel, self).__init__()
        # It is a 2D array of the table contents
        self.pressureMatrix = pressureMatrix
    def rowCount(self, parent=None):
        return len(self.pressureMatrix)
    def columnCount(self, parent=None):
        return len(self.pressureMatrix[0])
    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return self.pressureMatrix[index.row()][index.column()]
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignRight
    def headerData(self, section, orientation=Qt.Horizontal, role=Qt.DisplayRole):
        sectionList = [ QtTranslate('result_widget', 'Kör', None),
                        QtTranslate('result_widget', 'deltaPk (Pa)', None), # Pressure loss of path
                        QtTranslate('result_widget', 'deltaPbeszab;K (Pa)', None),
                        QtTranslate('result_widget', 'kv;beszab;K', None)]
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return sectionList[section]
