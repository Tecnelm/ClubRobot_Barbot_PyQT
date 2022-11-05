import sys
from PySide2 import QtCore, QtGui, QtWidgets
from Class.frame import MainWindow
import signal



signal.signal(signal.SIGINT, signal.SIG_DFL)
app = QtWidgets.QApplication(sys.argv)
window = MainWindow.MainWindow()
window.showFullScreen()
#window.show()
sys.exit(app.exec_())
