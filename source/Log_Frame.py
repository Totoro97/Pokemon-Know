import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Log_Frame(QWebEngineView):
	
	def __init__(self, father = None) :
		super().__init__(father)
		self.html = '<html><body style=\"color: #FFFFFF; font-family:Arial,Verdana,Sans-serif; background-color: #404040\">\n'
		self.refresh()
	
	def add_message(self, text) :
		self.html += '<div>' + text + '</div>\n'
		self.refresh()
		
	def refresh(self) :
		#for p, poke in poke_lis :
		#	html += '<div>' + '%.6f'%p + '  ' + poke + '</div>\n'
		#html += '</body></html>'
		self.setHtml(self.html + '</body></html>')
		self.show()
		
		
