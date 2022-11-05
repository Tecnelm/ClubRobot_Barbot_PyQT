from ..frame import MainWindow
from . import COMMANDE,VALUE
from ..led import PRESET
from typing import List
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt,SIGNAL,Signal,Slot
from PySide2.QtWidgets import *

from . import TIMEOUT_RESEND
class callback_receive():
    timerSTOPcmd :QtCore.QTimer
    def __init__(self,mainWindow:MainWindow):
        self.mainWindow = mainWindow
    pass

    def parse(self,commande,value):
        if(COMMANDE.RESPONSE == commande) :
            self.response(value)
        elif( COMMANDE.SEND_POSITON == commande):
            self.receive_position(value)
        elif (COMMANDE.STOP_GAME == commande ):
            self.stop_game(value)
        elif (COMMANDE.START_GAME == commande):
            self.start_Game(value)
        elif (COMMANDE.DEBUG_STR == commande):
            self.debug_str(value)
        elif (COMMANDE.STATE_GLASS == commande):
            self.state_glass(value)

    def response(self,value):
        pass


    def start_Game(self,value):
        self.mainWindow.gameWidget.set_game_status.emit(COMMANDE.START_GAME.value,value)
        self.mainWindow.callback_send.start_Game(VALUE.OK )


    def stop_game(self,value):
        if(value == VALUE.OK):
                self.mainWindow.callback_send.signalStop.emit()

    def debug_str(self,value):
        pass

    def state_glass(self,value):
        if (VALUE.KO.value == value):
            self.mainWindow.led.setPreset(PRESET.IDDLE)
        elif(value == VALUE.OK.value):
            self.mainWindow.led.setPreset(PRESET.IDDLE_GLASS)

    def receive_position(self, value):
        self.mainWindow.gameWidget.set_update_Score.emit(value)

    pass
