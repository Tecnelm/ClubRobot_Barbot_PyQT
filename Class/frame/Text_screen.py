import os
import random
from PySide2.QtWidgets import QLabel, QWidget
from PySide2.QtCore import Qt
from PySide2.QtGui import QFont, QImage, QPixmap
from ..frame import SCREEN_WIDTH,SCREEN_HEIGHT,POLICE_RULES_SIZE,URL_RULES

class Text_screen():
	"""TextScreen class"""

	def __init__(self,parent=None) -> None:
		"""Constructor of the class"""

		self.sign = QLabel(parent=parent)
		#QLabel showing the sign
		self.pixmap = QPixmap('data/test-sign.png')
		#Pixmap ofthe sign

		self.rules_label = QLabel(parent=parent)
		#QLabel showing the rule
		self.rules_label.setTextFormat(Qt.TextFormat.AutoText)
		#Set the text to be auto formated
		self.rules_label.setFont(QFont("BlackChancery",POLICE_RULES_SIZE))
		#Set the font of the text displayed in the object
		self.rules = self.import_text_files(URL_RULES)

		self.rules_label.setMaximumSize(SCREEN_WIDTH,SCREEN_HEIGHT)


		self.instruction = QLabel(parent=parent)
		#QLabel showing the rule
		self.instruction.setTextFormat(Qt.TextFormat.AutoText)
		#Set the text to be auto formated
		self.instruction.setFont(QFont("BlackChancery",POLICE_RULES_SIZE+10))
		#Set the font of the text displayed in the object

		self.instruction.setText("Mets ton verre et appuis sur les boutons")
		self.instruction.adjustSize();
		self.instruction.move((SCREEN_WIDTH-self.instruction.width())/2 , 10)


		self.sign_instr = QLabel(parent=parent)
		pixmap = self.pixmap.scaled(self.instruction.width()+40,self.instruction.height()+20)
		self.sign_instr.setPixmap(pixmap)
		self.sign_instr.move((SCREEN_WIDTH-self.instruction.width())/2 -20, 10)
		self.sign_instr.adjustSize()


#Import the text of all the rules


	def import_text_files(self, path:str) -> list:
		"""Return a list of all the text contain in all the file contain in the folder given with the path

		Args:
			path (str): Path of the folder

		Returns:
			list: List of all the text
		"""

		text_files = []
		for filename in os.listdir(path):

			with open(os.path.join(path, filename), 'r', encoding='utf8') as file:

				text = file.read()
				text_files.append(text)

		return text_files


	def show_rules(self) -> None:
		"""Write a random rule in a center of the screen with a sign behind"""

		text:str = random.choice(self.rules)

		self.rules_label.setAlignment(Qt.AlignCenter)
		self.rules_label.setText(text)
		self.rules_label.adjustSize()

		w:int = self.rules_label.width()
		h:int = self.rules_label.height()
		self.rules_label.move((SCREEN_WIDTH-w)/2 , (SCREEN_HEIGHT-h)/2)

		self.pixmap = self.pixmap.scaled(w + 50 , h + 50)
		self.sign.setAlignment(Qt.AlignCenter)
		self.sign.setPixmap(self.pixmap)
		self.sign.adjustSize()
		w:int = self.sign.width()
		h:int = self.sign.height()
		self.sign.move((SCREEN_WIDTH-w)/2 , (SCREEN_HEIGHT-h)/2)
		self.sign.show()
		self.rules_label.show()
		self.sign_instr.show()
		self.instruction.raise_()
		self.instruction.show()


	def hide(self) -> None:
		self.rules_label.hide()
		self.sign.hide()
		self.sign_instr.hide()
		self.instruction.hide()

