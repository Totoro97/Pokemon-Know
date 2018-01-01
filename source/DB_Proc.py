import os, sys, json

class DB_Proc :
	def __init__(self) :
		return
		
	def create_empty(self, url) :
		f = open(url, 'w')
		f.write('{}')
		f.close()
		return
		
	def add_attr(self, name, attr, val, p) :
		url = '../data/' + name + '.json'
		if not os.path.exists(url) :
			self.create_empty(url)
		f = open(url, 'r')
		f_str = f.read()
		f.close()
		data = json.loads(f_str)
		if attr not in data :
			data[attr] = dict()
		data[attr][val] = p
		f = open(url, 'w')
		f.write(json.dumps(data, ensure_ascii = False).replace('},', '},\n'))
		f.close()
	
if __name__ == '__main__' :
	db_proc = DB_Proc()
	db_proc.add_attr(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

