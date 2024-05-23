import pandas as pd

class RichICA:
    def __init__(self):
        self.importedFilename = ""

    def set_importedFilename(self, filename):
        self.importedFilename = filename

    def get_importedFilename(self):
        return self.importedFilename
