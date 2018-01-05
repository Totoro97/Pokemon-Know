import json
import os
import Certainty_Factor as cf

class Pokemon :
	
	def __init__(self, name) :
		self.load_data(name)
		self.p = 0.0
		self.cnt = 0
		self.false_cnt = 0
				
	def load_data(self, name) :
		f = open('../data/' + name + '.json', 'r')
		raw_data = json.loads(f.read())
		f.close()
		
		self.data = dict()
		for attr in raw_data :
			if attr == '继承' :
				continue
			self.data[attr] = dict()
			for val in raw_data[attr] :
				self.data[attr][val] = cf.w2cf[raw_data[attr][val]]
		
		if '继承' in raw_data :
			sing = raw_data['继承']
			for val in sing :
				self.update_inh(val, sing[val])
		
		self.ave_it()
	
	def update_inh(self, name, p) :
		url = '../data/' + name + '.json'
		if not os.path.exists(url) :
			return
			
		f = open(url, 'r')
		raw_data = json.loads(f.read())
		f.close()
		
		for attr in raw_data :
			if attr not in self.data :
				self.data[attr] = dict()
			for val in raw_data[attr] :
				if val not in self.data[attr] :
					self.data[attr][val] = cf.mix(0.0, raw_data[attr][val])
				else :
					self.data[attr][val] = cf.mix(self.data[attr][val], raw_data[attr][val])
	
	def ave_it(self) :
		for attr in self.data :
			for val in self.data[attr] :
				self.data[attr][val] /= len(self.data[attr])
	
	def is_out(self) :
		if self.false_cnt > 2 or (self.cnt > 5 and self.false_cnt > 1) :
			return True
		return False
		
	def update_p(self, attr, val, mark, rat = 1.0) :
		self.p = self.new_p(attr, val, mark, rat)
		self.cnt += 1
		if self.p < 0.5 :
			self.false_cnt += 1
		
	def new_p(self, attr, val, mark, rat = 1.0) :
		p = self.belong_val(attr, val, rat)
		if not mark :
			if p < 0 :
				p *= -0.5
			else :
				p = max(-0.9, p * (-1.5))
		#if val == '拉达' and mark:
		#	print(str(p) + '+' + str(list(self.data['名字'])[0]))
		return cf.mix(self.p, p)
	
	def belong_val(self, attr, val, rat = 1.0) :
		p = 0.0
		if attr not in self.data :
			p = -0.4
		elif val not in self.data[attr] :
			p = -0.8
		else :
			p = self.data[attr][val]
		return p * rat
