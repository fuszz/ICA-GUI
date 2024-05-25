import sys

from PyQt5 import QtWidgets

import front.gui as front
import back.richICA as back

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = front.Ui_MainWindow()
ui.setupUi(MainWindow)


backend = back.RichICA()

# Połączenia sygnałów!!!
#...

# Koniec połączeń sygnałów


backend.start()
MainWindow.show()
sys.exit(app.exec_())