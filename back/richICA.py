import pandas as pd
import back.oscillogramMpl as oscillogramMpl

class RichICA:
    def __init__(self):
        self.importedFilename = ""

    def set_importedFilename(self, filename):
        self.importedFilename = filename

    def get_importedFilename(self):
        return self.importedFilename

    def get_widget(self):
        return oscillogramMpl.OscillogramMpl().get_widget()

