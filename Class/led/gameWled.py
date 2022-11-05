import threading

from PySide2.QtCore import QObject,Signal,Slot
from . import PRESET

import requests


class wled():
    led_ip:str
    def __init__(self,ip):
        super(wled,self).__init__()
        self.led_ip = ip
        self.updatePreset = threading.Thread(target=self.callbackPreset)

    def setPreset(self,preset:PRESET):
        self.preset = preset.value
        if (not self.updatePreset.is_alive()):
            self.updatePreset.start()

    def callbackPreset(self):
        try:
            requests.get("http://"+self.led_ip+"/win&PL="+str(self.preset))
        except:
            pass
        self.updatePreset = threading.Thread(target=self.callbackPreset)
