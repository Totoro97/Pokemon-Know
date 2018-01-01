import Poke_Core
import sys, time
import copy
from functools import partial
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView

import Message_Frame, Poke_Core
#poke_core = Poke_Core.Poke_Core

ans = 'start'

class Main_Window(QMainWindow) :
	
	def __init__(self) :
		super().__init__()
		self.poke_core = Poke_Core.Poke_Core()
		self.message_frame = Message_Frame.Message_Frame(self)
		self.btn_wrapper = QWidget(self)
		#self.btn_1 = QPushButton('开始', self.btn_wrapper)
		#self.btn_1.clicked.connect(lambda: self.proc_ans('start'))
		self.init_UI()
		self.btn_pool = []
		self.gen_btns([('开始','start')])
		
	
	def init_UI(self) :
		self.setGeometry(10, 10, 800, 700)
		self.message_frame.setGeometry(10, 10, 340, 500)
		self.message_frame.add_message('hello', False)
		self.message_frame.add_message('hello', False)
		self.btn_wrapper.setGeometry(10, 520, 340, 35)
		#self.btn_1.setGeometry(0, 0, 340, 35)
		self.show()
	
	def gen_btns(self, options) :
		for _ in self.btn_pool :
			_.close()
		self.btn_pool = []
		size = len(options)
		width = int((340 - 5) / size)
		index = 0
		#print(width)
		self.options = options
		for _ in options :
			sing = QPushButton(_[0], self.btn_wrapper)
			print(_)
			#tmp = copy.copy(_)
			sing.clicked.connect(partial(self.proc_ans, _))
			sing.setGeometry(5 + index * width, 0, width - 5, 35)
			sing.show()
			self.btn_pool.append(sing)
			
			index += 1
		#print(self.btn_pool)
			
	def proc_ans(self, Ans) :
		Ans, ans = Ans
		self.message_frame.add_message(Ans, True)
		text, options = self.poke_core.proc(ans)
		self.message_frame.add_message(text, False)
		if (len(options) == 0) :
			self.close()
			exit()
		self.gen_btns(options)

app = QApplication(sys.argv)
main_window = Main_Window()
app.exec_()

