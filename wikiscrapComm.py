# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re
import io
from progress.bar import Bar

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}


url = "https://en.wikipedia.org/wiki/Mia_Khalifa"
queue = [] 	#Ουρά για το crawiling
queuetp = [] #Ουρα για την αποθηκευση
links = set() #Set για να μην εχω διπλοτυπα links
bar = Bar("Processing", max=200,suffix='%(percent)d%% [%(index)d / %(max)d]')
f = io.open("data.txt","w+", encoding="utf-8") #Ανοιγμα αρχείου το io ειναι για backward compability με python 2
for i in range (200):
	bar.next()
	r  = requests.get(url)
	soup = BeautifulSoup(r.content,'html.parser')
	news_links = soup.find_all("div",{'id':'bodyContent'}) #Περιχομενο article
	
	for div in news_links:	
		for link in div.find_all('a', href = re.compile("^/wiki")): #Regeg για μονο εσωτερικα links
			links.add(link.get('href')) #Προσθηκη link στο set
			
	for l in links:
		queue.append(l) #Προσθηκη των set στο queue
		
	urltp = queue.pop(0) #Αφερεση του πρωτου link απο το queue και αποθηκευση
	url = "https://en.wikipedia.org" + str(urltp) #Αλλαγη του url
	queuetp.append(urltp) #Προσθηκη του αφαιρεμενου url σε αλλο queue
	
bar.finish() #Τελος μπαρας

for q in queue:  #Προσθηκη των υπολοιπων στο νεο Queue
	queuetp.append(q)
	
for qtp in queuetp: #Αποθηκευση του νεου queue στο αρχειο με προθεμα
	f.write("https://en.wikipedia.org" + qtp + "\n")