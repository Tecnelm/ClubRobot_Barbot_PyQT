from enum import Enum


class COMMANDE(Enum):
    RESPONSE = 0
    SEND_POSITON = 1
    START_GAME = 2
    STOP_GAME = 3
    DEBUG_STR = 4
    STATE_GLASS = 5
    COUNT = 6

    def __eq__(self, other):
        return  self.value == other

class VALUE(Enum):
    NONE=0
    ERROR=1
    SERIAL_CONNECTED=2
    OK=3
    KO=4
    COUNT=5
    def __eq__(self, other):
        return  self.value == other



TIMEOUT_RESEND = 1000