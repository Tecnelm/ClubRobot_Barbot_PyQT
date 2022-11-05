import sys

from PySide2 import QtCore, QtGui, QtWidgets
from Class.frame import gameWidget
from ..serial import SerialCom
from ..callback import callbackReceive,callbackSend
from PySide2.QtCore import Signal,Slot
import signal
from ..callback import COMMANDE,VALUE

from . import IP_WLED


from ..led import gameWled,PRESET


class MainWindow(QtWidgets.QMainWindow):

    led : gameWled.wled
    def __init__(self):
        super().__init__()
        self.callback_receive = callbackReceive.callback_receive(self)
        self.serial = SerialCom.SerialCommunication( self.callback_receive)
        self.callback_send = callbackSend.callback_send(self.serial)

        self.led = gameWled.wled(IP_WLED)
        self.gameWidget = gameWidget.GameWidget( self.callback_send,led=self.led)
        self.layout().setMargin(0)
        self.layout().setSpacing(0)
        self.setCentralWidget(self.gameWidget)


        self.serial.read.start()

    def keyPressEvent(self, event):
        if  event.key() == QtCore.Qt.Key_Q :
            self.serial.stop()
            self.serial.serial.close()
            self.deleteLater()
            signal.raise_signal(signal.SIGINT)

        elif event.key() == QtCore.Qt.Key_Enter:
            self.updateSize()
        elif event.key() == QtCore.Qt.Key_A:
            self.callback_send.send_position(0)
        elif event.key() == QtCore.Qt.Key_Z:
            self.callback_receive.start_Game(VALUE.OK.value)
        elif event.key() == QtCore.Qt.Key_R:
            self.callback_receive.stop_game(VALUE.OK.value)
        elif event.key() == QtCore.Qt.Key_M:
            self.led.setPreset(PRESET.IDDLE)
        elif event.key() == QtCore.Qt.Key_L:
            self.led.setPreset(PRESET.IDDLE_GLASS)
        elif event.key() == QtCore.Qt.Key_B:
            self.callback_receive.receive_position(VALUE.OK.value)
        event.accept()
    def mousePressEvent(self, event:QtGui.QMouseEvent) -> None:
        if event.button() == QtCore.Qt.MouseButton.MidButton :
            self.serial.stop()
            self.serial.serial.close()
            self.deleteLater()
            signal.raise_signal(signal.SIGINT)


    def updateSize(self):
         self.gameWidget.updateSize()

    def resizeEvent(self, event):
        print("with ="+str(self.width()))
        print("height ="+str(self.height()))
        self.gameWidget.updateGraphique()
        pass

    def draw_something(self):
        painter = QtGui.QPainter(self.label.pixmap())
        painter.drawImage(0,0,self.test)
        painter.end()

