from PySide2 import QtCore,QtWidgets,QtGui
from . import GAME_MAX_TIME,Life,SCREEN_HEIGHT,SCREEN_WIDTH


class Cronometer(QtWidgets.QProgressBar):

    def __init__(self,parent=None):
        super(Cronometer, self).__init__(parent)
        self.setGeometry( 0, 0, 25, SCREEN_HEIGHT)
        self.setFixedSize(25,SCREEN_HEIGHT)
        self.setFont(QtGui.QFont("Arial",20))
        self.adjustSize()
        self.setOrientation(QtCore.Qt.Vertical)

    def updateTimer(self,value:int,):
        self.setFormat("Temps Restant: "+str(int(value/1000))+"s")
        self.setValue(int((value/GAME_MAX_TIME)*100))
        self.adjustSize()
        self.raise_()
        self.repaint()

