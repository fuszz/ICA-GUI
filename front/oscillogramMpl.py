import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as FigureCanvas,
                                                NavigationToolbar2QT as NavigationToolbar)
from PyQt5.QtCore import pyqtSignal


class OscillogramMpl(FigureCanvas):
    sel_range = pyqtSignal(float, float)

    def __init__(self, parent=None):
        fig, self.ax = plt.subplots()
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        # Generowanie sygnału
        czas = np.linspace(0, 111, 500, endpoint=False)
        sygnal = np.cos(2 * np.pi * 5 * czas)
        self.ax.plot(czas, sygnal, label='Sygnał')

        # Funkcja wywoływana po zaznaczeniu obszaru
        def onselect(min, max):
            self.sel_range.emit(min, max)
            print(f"Zaznaczony obszar od {min} do {max}")

        self.span = SpanSelector(self.ax, onselect, 'horizontal', useblit=True)
