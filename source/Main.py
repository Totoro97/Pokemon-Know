import Poke_Core
import sys, time
import copy
import json
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
		self.init()
	def init(self) :
		self.poke_core = Poke_Core.Poke_Core()
		self.message_frame = Message_Frame.Message_Frame(self)
		self.btn_wrapper = QWidget(self)
		#self.btn_1 = QPushButton('开始', self.btn_wrapper)
		#self.btn_1.clicked.connect(lambda: self.proc_ans('start'))
		self.init_UI()
		self.btn_pool = []
		self.gen_btns([('开始','start')])
		
	
	def init_UI(self) :
		self.setWindowTitle('Pokemon-Know')
		self.setGeometry(10, 10, 360, 565)
		self.setStyleSheet("QMainWindow {background: #4a4a4a;}")
		self.message_frame.setGeometry(10, 10, 340, 500)
		self.message_frame.add_message('Hi,我见到了一只Pokemon', True)
		self.message_frame.add_message('但是我不知道它到底是啥诶', True)
		self.message_frame.add_message('你能帮帮我吗？', True)
		self.message_frame.add_message('没问题', False)
		self.message_frame.add_message('但是我需要问你几个问题才能判断出是哪种Pokemon', False)
		self.message_frame.add_message('好的', True)
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
			sing.setStyleSheet("background: #303030; color: #FFFFFF; font-size: 15px")
			sing.show()
			self.btn_pool.append(sing)
			
			index += 1
		#print(self.btn_pool)
			
	def proc_ans(self, Ans) :
		Ans, ans = Ans
		if (ans == 'exit') :
			self.close()
			return
		if (ans == 'again') :
			self.init()
			return
		self.message_frame.add_message(Ans, True)
		text, options = self.poke_core.proc(ans)
		flg = False
		if (text[:6] == '<+img>') :
			pokemon, text = text[6:].split('<+img>')
			flg = True
		self.message_frame.add_message(text, False)
		if flg :
			f = open('../data/_poke_pic_url_.json', 'r')
			data = json.loads(f.read())
			f.close()
			url = 'https:' + data[pokemon]
			self.message_frame.add_message('<img src=\"%s\" width=\"200\" height=\"200\">'%url, False)
		if (len(options) == 0) :
			self.close()
			exit()
		self.gen_btns(options)

app = QApplication(sys.argv)
main_window = Main_Window()
app.exec_()

