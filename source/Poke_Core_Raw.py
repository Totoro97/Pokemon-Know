import csv

class Poke_Core :
	
	def __init__(self) :
		self.load_data()
	
	def load_data(self) :
		csvfile = open('../data/pokemon.csv','r')
		csvreader = csv.reader(csvfile)
		sing = True
		data = []
		self.attr_val = dict()
		for row in csvreader :
			if sing :
				self.attrs = list(row)
				for _ in self.attrs :
					self.attr_val[_] = set()
				sing = False
				continue
			just = dict()
			for index in range(len(self.attrs)):
				just[self.attrs[index]] = row[index].split(' ')
			data.append(just)
		csvfile.close()
		# data: [{'A':['a'], 'B','b'}, {..}, ..]
		self.pokemons = {}
		for pokemon in data :
			for _ in pokemon :
				for __ in pokemon[_] :
					self.attr_val[_].add(__)
			sing = pokemon.copy()
			sing.pop('名字')
			#print(pokemon)
			#print(pokemon['名字'])
			self.pokemons[pokemon['名字'][0]] = sing
		self.attr_val.pop('名字')
		self.attrs.remove('名字')
		
	def filt_pokemon(self, token) :
		del_lis = []
		if token == 'yes' :
			for pokemon in self.pokemons :
				if (self.clar_val not in self.pokemons[pokemon][self.clar_attr]) :
					del_lis.append(pokemon)
		else :
			for pokemon in self.pokemons :
				if (self.clar_val in self.pokemons[pokemon][self.clar_attr]) :
					del_lis.append(pokemon)
		for pokemon in del_lis :
			self.pokemons.pop(pokemon)
		print('del_lis:')
		print(del_lis)
		print('res = %d' % (len(self.pokemons)))
		
	def get_size_true(self, clar_attr, clar_val) :
		ans = 0
		for pokemon in self.pokemons :
			if (clar_val in self.pokemons[pokemon][clar_attr]) :
				ans += 1
		return ans
	
	def choose_question(self) : # ret: text, opetions
		size = len(self.pokemons)
		self.clar_attr = self.clar_val = ''
		sing = size + 100
		for clar_attr in self.attr_val :
			for clar_val in self.attr_val[clar_attr] :
				size_true = self.get_size_true(clar_attr, clar_val)
				if (max(size_true, size - size_true) < sing) :
					sing = max(size_true, size - size_true)
					self.clar_attr = clar_attr
					self.clar_val = clar_val
		self.attr_val[self.clar_attr].remove(self.clar_val)
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
			
