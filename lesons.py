# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import io

url = "https://www.iee.ihu.gr/udg_courses/"

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}
page = requests.get('https://www.iee.ihu.gr/en/udg_courses/',headers=header)
soup = BeautifulSoup(page.content,'html.parser')
f = io.open("lesons.txt","w+", encoding="utf-8")
tables = soup.find_all('table')
table = tables[6]
infos = list()
for tr in table.find_all('tr'):
	text = ""
	for td in tr.find_all('td'):
		if not td.find('strong'):
			text =  text + td.text + " "
	if not text == "":	
		infos.append(text)
for i in infos:
	f.write(i + "\n")