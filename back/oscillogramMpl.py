import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QVBoxLayout
from matplotlib.widgets import SpanSelector, Slider
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as FigureCanvas,
                                                NavigationToolbar2QT as NavigationToolbar)
from PyQt5 import QtWidgets


class OscillogramMpl(FigureCanvas):
    def __init__(self, parent=None):
        fig, self.ax = plt.subplots()
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        # Generowanie sygnału
        czas = np.linspace(0, 1, 500, endpoint=False)
        sygnal = np.cos(2 * np.pi * 5 * czas)
        self.ax.plot(czas, sygnal, label='Sygnał')

        # Funkcja wywoływana po zaznaczeniu obszaru
        def onselect(min, max):
            print(f"Zaznaczony obszar od {min} do {max}")

        self.span = SpanSelector(self.ax, onselect, 'horizontal', useblit=True)


    def get_widget(self):
        widget = QtWidgets.QWidget()
        layout = QVBoxLayout()
        layout.addWidget(NavigationToolbar(self, widget))
        layout.addWidget(self)
        widget.setLayout(layout)
        return widget

