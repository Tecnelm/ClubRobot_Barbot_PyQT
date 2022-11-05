import os
import sys

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtWidgets import *




class Background(QtWidgets.QLabel):
    frame = 0
    path = None
    backgroundList = []

    def __init__(self,path,parent = None):
        super(Background,self).__init__(parent)
        self.frame = 0
        self.path = path
        self.load()

    def load(self):
        url = []
        for file in os.listdir(self.path):
            if(file.endswith(".jpg")):
                url.append(file)
        url.sort()
        for image in url:
            self.backgroundList.append(QtGui.QImage(self.path+image))

    def updateSize(self,width = 0,heigh = 0):

        for i in range (len(self.backgroundList)):
            image:QtGui.QImage = self.backgroundList[i]
            self.backgroundList[i] = image.scaled(width, heigh)




    def step(self):
        self.frame  = self.frame+1
        if(self.frame >= len(self.backgroundList)):
            self.frame = 0

    def updatePos(self):
         self.setPixmap(QtGui.QPixmap(self.backgroundList[self.frame]))
         self.update()

