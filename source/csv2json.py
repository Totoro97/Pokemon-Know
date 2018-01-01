import json, csv
csvfile = open('../data/pokemon.csv','r')
csvreader = csv.reader(csvfile)
sing = True
data = []
for row in csvreader :
	if sing :
		attrs = list(row)
		sing = False
		continue
	just = dict()
	for index in range(len(attrs)):
		vals = row[index].split(' ')
		if vals == [''] : 
			continue
		just[attrs[index]] = dict()
		for _ in vals :
			if (index == 0) :
				just[attrs[index]][_] =  'defi'
			else :
				just[attrs[index]][_] = 'prob'
	name = list(just['名字'])[0]
	f = open('../data/' + name + '.json', 'w')
	f.write(json.dumps(just, ensure_ascii = False).replace('},', '},\n'))
	f.close()
csvfile.close()
