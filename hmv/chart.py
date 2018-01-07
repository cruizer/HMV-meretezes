# -*- coding: utf-8 -*-
# embedding_in_qt4.py --- Simple Qt4 application embedding matplotlib canvases
#
# Copyright (C) 2005 Florent Rougon
#               2006 Darren Dale
#
# This file is an example program for matplotlib. It may be used and
# modified with no restriction; raw copies as well as modified versions
# may be distributed without limitation.

from __future__ import unicode_literals
from PyQt4 import QtGui

import numpy as np
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class HMVBaseCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        # We want the axes cleared every time plot() is called
        self.axes.hold(False)

        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent) # pylint: disable=E1101

        FigureCanvas.setSizePolicy(self, # pylint: disable=E1101
                                   QtGui.QSizePolicy.Expanding, # pylint: disable=E1101
                                   QtGui.QSizePolicy.Expanding) # pylint: disable=E1101
        FigureCanvas.updateGeometry(self) # pylint: disable=E1101

    def compute_initial_figure(self):
        pass


class PipeFlowChartCanvas(HMVBaseCanvas):
    """Simple canvas with a sine plot."""
    def __init__(self, flowData, parent=None):
        self.flowData = flowData
        super(PipeFlowChartCanvas, self).__init__(parent)
    def compute_initial_figure(self):
        y_pos = np.arange(len(self.flowData)) # pylint: disable=E1101

        self.axes.bar(y_pos, self.flowData, align='center', alpha=0.4)
        self.axes.set_xticks(y_pos)
        self.axes.set_xticklabels(['F' + str(nr) for nr in np.arange(len(self.flowData))]) # pylint: disable=E1101
        self.axes.set_ylabel('Térfogatáram (dm3/h)')
        self.axes.set_xlabel('Felszálló ágak')
        self.axes.set_title('Felszállók térfogatárama')
        self.axes.grid(True)
