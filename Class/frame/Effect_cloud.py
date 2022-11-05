
import os
import sys
import random
import threading
import time

from PySide2 import QtCore, QtGui, QtWidgets


from Class.frame import CLOUD_URL,SCREEN_WIDTH,SCREEN_HEIGHT



class Effect_cloud(QtWidgets.QLabel):

    Opacity = 0
    effect:threading.Thread
    OPACITY_INC = 10
    OPACITY_MAX = 80
    OPACITY_MIN = 0
    CHANGE_TIME_MS = 20

    def __init__(self, parent=None):
        super(Effect_cloud, self).__init__(parent)
        image=QtGui.QImage(CLOUD_URL)
        image.scaled(SCREEN_WIDTH,SCREEN_HEIGHT)
        self.setPixmap(QtGui.QPixmap(image))
        self.move(-100,-100)
        self.adjustSize()
        self.setWindowOpacity(self.OPACITY_MAX)