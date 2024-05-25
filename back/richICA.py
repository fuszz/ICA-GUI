from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
import back.oscillogramMpl as oscillogramMpl


class RichICA(QThread):



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

    def run(self):
        while True:
            pass

    def importFilename(self, filename):
        self.importedFilename = filename
        # Wczytywanie danych z pliku .csv

    def get_importedFilename(self):
        return self.importedFilename

    def set_oscillogram(self):
        pass

    def get_oscillogram(self):
        return self.oscillogram.get_widget()
