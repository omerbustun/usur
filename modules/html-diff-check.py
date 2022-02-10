# LIBS
import requests,os
from bs4 import BeautifulSoup

# VARIABLE TO BE TAKEN
site = "google.com" 

# 4 FILE WITHOUT ':'
x = site.index(":")
domain = site[x+3:]

# FILE NAMES
base_html = domain+"_base.txt"
temp_html = domain+"_temp.txt"

# CHECKING BASE HTML TEXT
def check_base(site):
	if os.path.exists(base_html):
		return 1
	else:
		return 0

# GETTING BASE HTML CODES
def get_base_html(site):
	response = requests.get(site)
	#html = response.content
	soup = BeautifulSoup(response.content, 'html.parser')

	f = open(base_html, "w")
	f.write(str(soup.prettify()))
	f.close()

# GETTING TEMP HTML CODES FOR COMPARING
def get_temp_html(site):
	response = requests.get(site)
	#html = response.content
	soup = BeautifulSoup(response.content, 'html.parser')
	f = open(temp_html, "w")
	f.write(str(soup.prettify()))
	f.close()

# MAIN
if (check_base(site) == 0):
	get_base_html(site)
else:
	get_temp_html(site)
	# reading files
	f1 = open(base_html, "r")
	f2 = open(temp_html, "r")

	i = 0

	for line1 in f1:
		i += 1
	
		for line2 in f2:
		
			# matching line1 from both files
			if line1 == line2:
				# print IDENTICAL if similar
				print("Line ", i, ": IDENTICAL")	
			else:
				print("Line ", i, ":")
				# else print that line from both files
				print("\tFile 1:", line1, end='')
				print("\tFile 2:", line2, end='')
			break

	# closing files
	f1.close()									
	f2.close()
	# deleting temp file
	os.remove(temp_html)							

