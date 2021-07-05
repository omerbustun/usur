# LIBS
import requests,os
from bs4 import BeautifulSoup

# VARIABLE TO BE TAKEN
site = "https://tedu.edu.tr" 

# 4 FILE WITHOUT ':'
x = site.index(":")
domain = site[x+3:]

# FILE NAME
base_html = domain+"_base.txt"

def update_base(site):
	if os.path.exists(base_html):
		response = requests.get(site)
		soup = BeautifulSoup(response.content, 'html.parser')
		f = open(base_html, "w")
		f.write(str(soup.prettify()))
		f.close()
	else:
		#error report
		print("base html file does not exist!")

update_base(site)
