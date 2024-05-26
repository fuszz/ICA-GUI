import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtCore import pyqtSignal


class OscillogramMpl(FigureCanvas):

    sel_range = pyqtSignal(float, float)

    def __init__(self, parent=None):
        fig, self.ax = plt.subplots()
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        def onselect(min, max):
            self.sel_range.emit(min, max)
            print(f"Zaznaczony obszar od {min} do {max}")

        self.span = SpanSelector(self.ax, onselect, 'horizontal', useblit=True)

    def updateOscillogram(self, data: pd.DataFrame):
        self.canvas.figure.clear()
        self.ax = plt.plot(data)
        self.canvas.draw()
