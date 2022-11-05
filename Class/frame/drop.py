
import os
import sys
import random

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtWidgets import *

from Class.frame import GAME_DROP_SPEED,DROP_WIDTH,DROP_HEIGHT



class DropImage():
    imageList =[]
    def __init__(self, path):
        super(DropImage, self).__init__()
        self.path = path
        self.load()
        self.resize(DROP_WIDTH,DROP_HEIGHT)


    def load(self):
        url = []
        for file in os.listdir(self.path):
            if (file.endswith(".png")):
                url.append(file)

        for image in url:
            self.imageList.append(QtGui.QImage(self.path + image))

    def resize(self, width=0, heigh=0):
        for i in range(len(self.imageList)):
            image: QtGui.QImage = self.imageList[i]
            self.imageList[i] = image.scaled(width, heigh)


    def getImage(self)->QtGui.QPixmap:
        id = int(random.randint(0, len(self.imageList)-1))
        return QtGui.QPixmap(self.imageList[id])


class Drop(QtWidgets.QLabel):
    path = None
    xPos = 0
    yPos = 0
    pos = 0
    speed = 0

    def __init__(self, pos,xpos, dropImageList: DropImage, parent=None):
        super(Drop, self).__init__(parent)
        self.dropImage = dropImageList
        self.xPos = xpos
        self.speed = GAME_DROP_SPEED
        self.pos = pos

        self.setPixmap(dropImageList.getImage())
        self.adjustSize()
        self.yPos = -self.height()
        self.move(self.xPos,self.yPos)
        self.show()



    def step(self):
        self.yPos = self.yPos + self.speed

    def updatePos(self):
        self.move(self.xPos,self.yPos)
        self.update()

