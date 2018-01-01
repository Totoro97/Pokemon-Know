import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Message_Frame(QWebEngineView):
	
	def __init__(self, father = None) :
		super().__init__(father)
		self.Ahead = '<div class="bubbleItem"><span class="bubble leftBubble">\n'
		self.Atail = '\n<span class="bottomLevel"></span><span class="topLevel"></span></span></div>'
		self.Bhead = '<div class="bubbleItem clearfix"><span class="bubble rightBubble">\n'
		self.Btail = '\n<span class="bottomLevel"></span><span class="topLevel"></span></span></div>'
		self.messages = ''
		html_file = open('Message_Frame_Begin.html', 'r')
		self.html_text = html_file.read()
		html_file.close()
		self.init_UI()
		
	def init_UI(self) :
		#self.setGeometry(0, 0, 240, 400)
		self.setHtml(self.html_text + '</body></html>')
		self.show()

	def add_message(self, text, mark) :
		if not mark :
			text = self.Ahead + text + self.Atail
		else :
			text = self.Bhead + text + self.Btail
		self.messages += '\n' + text + '\n'
		#print(self.html_text + self.messages + '</body></html>')
		self.setHtml(self.html_text + self.messages + '</body></html>')
		#self.reload()
		#self.update()
if __name__ == '__main__' :
	app = QApplication(sys.argv)
	example = Message_Frame()
	sys.exit(app.exec_())
