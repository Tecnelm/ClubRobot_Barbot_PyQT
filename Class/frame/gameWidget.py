import random
import sys
from typing import List
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt,SIGNAL,Signal,Slot
from PySide2.QtWidgets import *
from Class.frame import background, drop, BACKGROUND_URL, DROP_URL, GAME_NB_POSITION, GAME_MAX_DROP, SCREEN_WIDTH, \
    SCREEN_HEIGHT,GAME_MAX_TIME

from Class.frame import game_state,Life,Cronometre,Effect_cloud,GAME_BLUR_IDDLE,GAME_BLUR_INGAME,DROP_HEIGHT


from . import GAME_UPDATE_DROP_TIMER,GAME_UPDATE_BACKGROUND_TIMER,GAME_UPDATE_SCREEN_TIMER,MAX_SCORE,MAX_VALUE_TIME

from . import Text_screen

from ..callback import callbackSend,COMMANDE,VALUE
from ..led import gameWled,PRESET


class GameWidget(QtWidgets.QWidget):
    background:background.Background
    dropList:List[drop.Drop] = []
    set_game_status = Signal(int,int)
    set_update_Score = Signal(int)
    game_status : game_state = game_state.GAME_INIT
    testDrop = None
    led:gameWled.wled
    score:Life.Score
    cronometer:Cronometre.Cronometer
    cloud:Effect_cloud.Effect_cloud
    effect_blur:QGraphicsBlurEffect
    progressBar:QtWidgets.QProgressBar


    def __init__(self,callback:callbackSend.callback_send,led:gameWled.wled,parent= None):
        super(GameWidget,self).__init__(parent)
        self.callback = callback
        self.background = background.Background(BACKGROUND_URL)
        self.background.updateSize(SCREEN_WIDTH,SCREEN_HEIGHT)
        self.led = led

        layout = QVBoxLayout()  # Create a layout.
        layout.addWidget(self.background)
        layout.setMargin(0)
        layout.setSpacing(0)
        self.setLayout(layout)  # Pass the layout to the window

        self.dropImage = drop.DropImage(DROP_URL)


        self.timer_drop = QtCore.QTimer(self)
        self.connect(self.timer_drop, SIGNAL('timeout()'), self.dropUpdate)
        self.timer_drop.interval()
        self.timer_drop.setInterval(GAME_UPDATE_DROP_TIMER)

        self.timer_background = QtCore.QTimer(self)
        self.connect(self.timer_background, SIGNAL('timeout()'), self.updateBackground)
        self.timer_background.interval()
        self.timer_background.setInterval(GAME_UPDATE_BACKGROUND_TIMER)

        self.timer_graphique = QtCore.QTimer(self)
        self.connect(self.timer_graphique, SIGNAL('timeout()'), self.updateGraphique)
        self.timer_graphique.interval()
        self.timer_graphique.setInterval(GAME_UPDATE_SCREEN_TIMER)

        self.time_end_game = QtCore.QTimer(self)
        self.connect(self.time_end_game,SIGNAL("timeout()"),self.set_status_end)
        self.time_end_game.setSingleShot(True)
        self.time_end_game.setInterval(GAME_MAX_TIME)


        self.set_game_status.connect(self.change_game_status)


        self.score = Life.Score(parent=self)
        self.rules = Text_screen.Text_screen(parent=self) # j'ai ajouté là !!!!
        self.set_update_Score.connect(self.updateScore)

        self.cronometer = Cronometre.Cronometer(parent=self)
        self.cronometer.updateTimer(0)
        self.cronometer.hide()
        self.timer_graphique.start()
        self.timer_background.start()
        self.game_status = game_state.GAME_IDDLE

        self.score.show()
        self.rules.show_rules() # et la pour show pour tester
        self.effect_blur = QGraphicsBlurEffect(self.background)
        self.effect_blur.setBlurRadius(GAME_BLUR_IDDLE)
        self.background.setGraphicsEffect(self.effect_blur)

        self.rules.show_rules()
        self.background.update()

        self.update()



    def updateSize(self):
        self.background.updateSize(SCREEN_WIDTH,SCREEN_HEIGHT)

    def set_status_end(self):
        self.time_end_game.stop()
        self.game_status = game_state.GAME_END


    def startGame(self):
        self.game_status = game_state.GAME_RUN
        self.led.setPreset(PRESET.IN_GAME)
        self.score.reset()
        self.timer_drop.start()
        self.time_end_game.start()
        self.cronometer.updateTimer(self.time_end_game.remainingTime())
        self.cronometer.show()
        self.effect_blur.setBlurRadius(GAME_BLUR_INGAME)
        self.rules.hide()








    def stopGame(self):
        self.timer_drop.stop()
        for drop in self.dropList:
            drop.hide()
            drop.destroy()
        self.dropList.clear()
        self.game_status = game_state.GAME_IDDLE
        self.cronometer.hide()
        self.effect_blur.setBlurRadius(GAME_BLUR_IDDLE)
        self.rules.show_rules()
        val = (self.score.score * MAX_VALUE_TIME)/MAX_SCORE
        self.callback.stop_Game(val)
        self.led.setPreset(PRESET.IDDLE)


    @Slot(int,int)
    def change_game_status(self,cmd:int,value:int):
        if (COMMANDE.START_GAME == cmd and VALUE.OK == value):
            if(self.game_status == game_state.GAME_IDDLE):
                self.startGame()
        elif (COMMANDE.STOP_GAME == cmd and VALUE.OK == value):
            pass
           # self.stopGame()

    @Slot(int)
    def updateScore(self,value):
        if(self.game_status == game_state.GAME_RUN or self.game_status == game_state.GAME_END):
            if(value == VALUE.OK.value):
                self.score.updateScore()

    def addDrop(self):
        pos = random.randint(0,GAME_NB_POSITION-1)
        posx = int(pos*self.width()/(GAME_NB_POSITION))
        pos = (GAME_NB_POSITION-1) - pos
        self.dropList.append(drop.Drop(pos,posx, self.dropImage,parent=self))

    def dropUpdate(self):
        removedrop = []
        for drop in self.dropList:
            drop.step()
            if(drop.yPos > self.height()-drop.height()):
                removedrop.append(drop)
                self.callback.send_position(drop.pos)
        for drop in removedrop:
            self.dropList.remove(drop)
            drop.deleteLater()


        if (self.game_status == game_state.GAME_RUN ):
            if len(self.dropList) == 0:
                self.addDrop()
            elif len(self.dropList) < GAME_MAX_DROP and self.dropList[-1].yPos > self.height()/GAME_MAX_DROP:
                self.addDrop()
        elif (self.game_status == game_state.GAME_END):
            if(len(self.dropList) == 0):
                self.stopGame()



    def updateBackground(self):
        self.background.step()


    def updateGraphique(self):
        for drop in self.dropList:
            drop.updatePos()
        self.background.updatePos()
        self.cronometer.updateTimer(self.time_end_game.remainingTime())



