import csv
import os
import math
import Certainty_Factor as cf
import Pokemon

class Poke_Core :
	
	def __init__(self) :
		self.load_data()
	
	def load_data(self) :
		file_lis = os.listdir('../data')
		self.pokemons = dict()
		self.attr_val = dict()
		for f_name in file_lis :
			if f_name[-5:] != '.json' : 
				continue
			self.pokemons[f_name[:-5]] = Pokemon.Pokemon(f_name[:-5])
		
		for pokemon in self.pokemons :
			for attr in self.pokemons[pokemon].data:
				if attr not in self.attr_val :
					self.attr_val[attr] = set()
				for val in self.pokemons[pokemon].data[attr] :
					self.attr_val[attr].add(val)
		del_lis = ['名字', '地区']
		for _ in del_lis :
			self.attr_val.pop(_)
		
	def filt_pokemon(self, token) :
		del_lis = []
		for pokemon in self.pokemons :
			self.pokemons[pokemon].p = self.pokemons[pokemon].new_p(self.clar_attr, self.clar_val, token == 'yes')
			if self.pokemons[pokemon].p < 0.5 :
				self.pokemons[pokemon].cnt += 1
			if self.pokemons[pokemon].cnt > 2 :
				del_lis.append(pokemon)
		for pokemon in del_lis :
			self.pokemons.pop(pokemon)
			
	def count_info(self, clar_attr, clar_val) :
		p_true = 0.0
		p_false = 0.0
		info_true = 0.0
		info_false = 0.0
		entr_true = 0.0
		entr_false = 0.0
		
		for pokemon in self.pokemons :
			if (self.pokemons[pokemon].belong_val(clar_attr, clar_val) > 0.0) :
				p_true += pow(cf.base, self.pokemons[pokemon].p)
			else :
				p_false += pow(cf.base, self.pokemons[pokemon].p)
				
		for pokemon in self.pokemons :
			#sing = self.pokemons[pokemon].belong_val(clar_attr, clar_val)
			#if (sing > 0) :
			#	p_true += sing
			#else :
			#	p_false -= sing			
			new_p = self.pokemons[pokemon].new_p(clar_attr, clar_val, True)
			info_true += pow(cf.base, new_p)
			new_p = self.pokemons[pokemon].new_p(clar_attr, clar_val, False)
			info_false += pow(cf.base, new_p)
		
		for pokemon in self.pokemons :
			new_p = self.pokemons[pokemon].new_p(clar_attr, clar_val, True)
			p = pow(cf.base, new_p) / info_true
			entr_true -= p * math.log2(p)
			new_p = self.pokemons[pokemon].new_p(clar_attr, clar_val, False)
			p = pow(cf.base, new_p) / info_false
			entr_false -= p * math.log2(p)
		
		ans = -(entr_true * p_true + entr_false * p_false) / (p_true + p_false) 
		#print('attr %s, val %s, p_true %.6f p_false %.6f entro = %.6f'%(clar_attr, clar_val, p_true, p_false, ans))
		#p_true = pow(cf.base, p_true)
		#p_false = pow(cf.base, p_false)
		return ans
		
			
	def choose_question(self) : # ret: text, opetions
		self.clar_attr = self.clar_val = ''
		sing = -10000000.0
		for clar_attr in self.attr_val :
			for clar_val in self.attr_val[clar_attr] :
				info = self.count_info(str(clar_attr), str(clar_val))
				#print(info)
				if (info > sing) :
					sing = info
					self.clar_attr = clar_attr
					self.clar_val = clar_val	
		self.attr_val[self.clar_attr].remove(self.clar_val)
		print("entropy: ", sing)
		#del_lis = []
		#for pokemon in self.pokemons :
		#	if (self.pokemons[pokemon].p < -0.7) :
		#		del_lis.append(pokemon)
		#for pokemon in del_lis :
		#	self.pokemons.pop(pokemon)	
		for pokemon in self.pokemons :
			print(pokemon + ':' + str(self.pokemons[pokemon].p))
		return '它的' + self.clar_attr + '是' + self.clar_val + '吗？', [('是的','yes'), ('不是','no')]
				
	def proc(self, token) : # ret: text, options
		if token != 'start' :
			self.filt_pokemon(token)
		if token == 'exit' :
			return '', []
		if (len(self.pokemons) == 1) :
			just = ''
			for _ in self.pokemons :
				just = _
				print(_)
			return '是不是' + str(just) + '?', [('是的', 'exit')]
		return self.choose_question()
			
