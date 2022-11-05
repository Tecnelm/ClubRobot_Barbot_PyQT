from ..serial import SerialCom
from . import COMMANDE,VALUE,TIMEOUT_RESEND
from PySide2 import QtCore




class callback_send(QtCore.QObject):

    timerStop_resend:QtCore.QTimer
    signalStop = QtCore.Signal()
    lastvalue=0;
    def __init__(self,Serial:SerialCom.SerialCommunication):
        super(callback_send, self).__init__()
        self.serial = Serial.serial
        self.signalStop.connect(self.stopSend)


        self.timerStop_resend = QtCore.QTimer(None)
        self.timerStop_resend.interval()
        self.timerStop_resend.setInterval(TIMEOUT_RESEND)
        self.connect(self.timerStop_resend, QtCore.SIGNAL('timeout()'), self.stopnewEmit)

    def send_position(self,value:int):
        try:
            self.serial.write(("{commande="+str(COMMANDE.SEND_POSITON.value)+";value="+str(value)+"}").encode())
            print("{commande="+str(COMMANDE.SEND_POSITON)+";value="+str(value)+"}")
        except:
            print("ERROR SERIAL RESTART")

    def stop_Game(self,value):
        try:
            self.timerStop_resend.start()
            self.lastvalue = value
            self.serial.write(("{commande="+str(COMMANDE.STOP_GAME.value)+";value="+str(value)+"}").encode())
            print("{commande="+str(COMMANDE.STOP_GAME)+";value="+str(value)+"}")
        except:
            print("ERROR SERIAL RESTART")

    def stopnewEmit(self):
        self.stop_Game(self.lastvalue)

    def start_Game(self,value:VALUE):
        try:
            self.serial.write(("{commande="+str(COMMANDE.START_GAME.value)+";value="+str(value.value)+"}").encode())
            print("{commande="+str(COMMANDE.START_GAME)+";value="+str(value)+"}")
        except:
            print("ERROR SERIAL RESTART")


    @QtCore.Slot()
    def stopSend(self):
        self.lastvalue = 0
        self.timerStop_resend.stop()




