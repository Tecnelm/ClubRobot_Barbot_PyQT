import serial
import threading
from . import SERIAL_PORT_NAME,TIMEOUT,BAUDRATE
from ..callback import callbackReceive



class SerialCommunication():
    serial:serial.Serial
    read:threading.Thread = None
    commande:str = ""
    flagKill = False


    def __init__(self,callbackReceive:callbackReceive.callback_receive,):
        self.read= threading.Thread(target=self.read_serial)
        self.callback = callbackReceive
        self.connect()


    def connect(self):
        self.serial = serial.Serial(SERIAL_PORT_NAME,BAUDRATE,timeout=TIMEOUT)
        while(not self.serial.isOpen()):
            self.serial.open()
    def read_serial(self):
        while not self.flagKill :
            try :

                st = self.serial.read(1).decode()
                self.commande =  self.commande.__add__(st)
                if(self.commande.endswith("}")):
                    print("Receive Commande :"+self.commande)
                    self.parseCommande(self.commande)
                    self.commande =""
            except:
                pass
        self.serial.close()
    def stop(self):
        self.flagKill = True
    def parseCommande(self, commande:str):
        if (commande.startswith("{") and commande.endswith("}")):
            cmd = commande.replace("{","").replace("}","").split(";")
            if len(cmd) == 2:
                cmdValue = int(cmd[0].split("=")[1])
                value = int(cmd[1].split("=")[1])
                self.callback.parse(cmdValue,value)



