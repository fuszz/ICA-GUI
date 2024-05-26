import sys
from PyQt5 import QtWidgets
import front.gui as front
import back.richICA as back

sys.path.append('front/')
sys.path.append('back/')

app = QtWidgets.QApplication(sys.argv)
window = front.MainWindow()

backend = back.RichICA()

# Połączenia sygnałów!!!
#  z frontendu na backend:

window.sigIcaRunningRequest.connect(backend.run_ica)
window.sigImportFileRequest.connect(backend.import_file)
window.sigProvideSelectedRangeRequest.connect(backend.get_last_selection_range)

window.sigSelBegSet.connect(backend.set_confirmed_selection_begin)
window.sigSelEndSet.connect(backend.set_confirmed_selection_end)

window.sigSamplingSet.connect(backend.set_sampling)
window.sigSampleNumSet.connect(backend.set_sample_num)


# --> z back na front

backend.sigLastSelectedRange.connect(front.MainWindow.set_selected_range)
# Koniec połączeń sygnałów

window.show()
backend.start()
sys.exit(app.exec_())