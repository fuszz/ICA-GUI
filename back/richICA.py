from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtWidgets
import front.oscillogramMpl as oscillogramMpl
import pandas as pd
import back.csv_handling as csv
import front.oscillogramMpl as oscillogram


class RichICA(QThread):
    sigLastSelectedRange = pyqtSignal(float, float)
    sigSendingDataframe = pyqtSignal(pd.DataFrame)

    def __init__(self):
        QThread.__init__(self)

        self.importedFilename = ""

        self.selectionBegin = 0.0
        self.selectionEnd = 0.0

        self.oscillogram = oscillogramMpl.OscillogramMpl()
        self.data = pd.DataFrame()

        self.sampling = 0
        self.sampleNum = 0

   # def run(self):
   #     while True:
   #         pass

    def import_file(self, filename):
        self.importedFilename = filename
        self.data = csv.csv_import(filename)
        self.sigSendingDataframe.emit(self.data)

    def run_ica(self):
        pass

    def set_sample_num(self, value):
        self.sampleNum = value
        print("Sample Num: ", self.sampleNum)

    def set_sampling(self, value):
        self.sampling = value

    def set_confirmed_selection_begin(self, value):
        self.selectionBegin = value

    def set_confirmed_selection_end(self, value):
        self.selectionEnd = value
