from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt,SIGNAL,Signal,Slot
from PySide2.QtWidgets import *
from . import PEPITE_URL,SCREEN_WIDTH,SCREEN_HEIGHT


class Score(QtWidgets.QWidget):
    score:int = 0
    txtLabel:QLabel
    def __init__(self,parent=None):
        super(Score, self).__init__(parent=parent)
        layout = QHBoxLayout();
        image = QtGui.QImage(PEPITE_URL)
        image = image.scaled(100,100)
        imageLabel = QtWidgets.QLabel(self)
        imageLabel.setPixmap(QtGui.QPixmap(image))
        self.adjustSize()

        self.txtLabel = QtWidgets.QLabel(self)
        self.txtLabel.setText("<font color='white'>"+str(self.score)+"</font>")

        self.txtLabel.setFont(QtGui.QFont("Arial",50))

        layout.addWidget(imageLabel)
        layout.addWidget(self.txtLabel)

        self.setLayout(layout)
        print(parent.width())
        self.adjustSize()
        self.move(SCREEN_WIDTH-self.width(),SCREEN_HEIGHT-self.height())
        self.show()

    def reset(self):
        self.score = 0
        self.txtLabel.setText("<font color='white'>"+str(self.score)+"</font>")

    def updateScore(self):
        self.score = self.score+1
        self.txtLabel.setText("<font color='white'>"+str(self.score)+"</font>")
        self.txtLabel.adjustSize()
        self.adjustSize()
        self.raise_()
        self.move(SCREEN_WIDTH-self.width(),SCREEN_HEIGHT-self.height())


def __str__(self):
            return str(self.score)
