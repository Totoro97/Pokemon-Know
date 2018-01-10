import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Poke_List(QWebEngineView):
	
	def __init__(self, father = None) :
		super().__init__(father)
		
	def refresh(self, poke_lis) :
		html = '<html><body style=\"color: #FFFFFF; font-family:Arial,Verdana,Sans-serif; background-color: #404040\">\n'
		for p, poke in poke_lis :
			html += '<div>' + '%.6f'%p + '  ' + poke + '</div>\n'
		html += '</body></html>'
		self.setHtml(html)
		self.show()
		
		
