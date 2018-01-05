from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pickle as pk
import os, time, re
from urllib.request import urlretrieve
import json
input_file = open('../data/pokemons.in', 'r')
input_str = input_file.read()
pokemons = input_str.split('\n')
input_file.close()

input_file = open('../data/pokemons.en','r')
input_str = input_file.read()
pokemons_en = input_str.split('\n')
input_file.close()

pokemons = zip(pokemons, pokemons_en)
driver = webdriver.Chrome()

url = 'https://wiki.52poke.com/wiki/'

index = 0

def proc(index) :
	return str(index).zfill(3)
	

for pokemon, en in pokemons :
	index += 1
	if pokemon == '' or en == '' :
		continue
	f = open('../data/_poke_pic_url_.json', 'r')
	data = json.loads(f.read())
	f.close()
	if (pokemon in data) :
		continue
	driver.get(url + pokemon)
	html = driver.page_source
	soup = bs(html)
	file_name = proc(index) + en + '.png'
	x = soup.find(alt = file_name)
	data[pokemon] = str(x['data-url'])
	f = open('../data/_poke_pic_url_.json', 'w')
	f.write(json.dumps(data, ensure_ascii = False).replace('},', '},\n'))
	f.close()
	# urlretrieve('https:' + str(x['data-url']), '../data/pic/' + pokemon + '.png')
	time.sleep(2)
