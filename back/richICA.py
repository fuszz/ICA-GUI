from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtWidgets
import front.oscillogramMpl as oscillogramMpl


class RichICA(QThread):
    sigLastSelectedRange = pyqtSignal(float, float)
    sigSendingOscillogram = pyqtSignal(QtWidgets.QWidget)

    def __init__(self):
        QThread.__init__(self)

        self.importedFilename = ""

        self.lastSelectionBegin = 0.0
        self.lastSelectionEnd = 0.0

        self.confirmedSelectionBegin = 0.0
        self.confirmedSelectionEnd = 0.0

        # Obsługa oscylogramów jest jeszcze zdecydowanie do dopisania!!!
        self.oscillogram = oscillogramMpl.OscillogramMpl()
        self.oscillogramData = 0  # To do zmiany potem

        self.sampling = 0
        self.sampleNum = 0

    def run(self):
        while True:
            pass
    def import_file(self, filename):
        self.importedFilename = filename
        # Wczytywanie danych z pliku .csv

    def get_imported_file(self):
        return self.importedFilename

    def get_oscillogram(self):
        print("Otrzymano sygnał")
        self.sigSendingOscillogram.emit(self.oscillogram.get_widget())
        print("Wysyłam oscylogram")

    def run_ica(self):
        pass

    def get_last_selection_range(self):
        self.confirmedSelectionBegin = self.lastSelectionBegin
        self.confirmedSelectionEnd = self.lastSelectionEnd
        self.sigLastSelectedRange.emit(self.confirmedSelectionBegin, self.confirmedSelectionEnd)

    def set_sample_num(self, value):
        self.sampleNum = value
        print("Sample Num: ", self.sampleNum)

    def set_sampling(self, value):
        self.sampling = value

    def set_confirmed_selection_begin(self, value):
        self.confirmedSelectionBegin = value

    def set_confirmed_selection_end(self, value):
        self.confirmedSelectionEnd = value
