from requests_html import HTMLSession
import json
import requests
from bs4 import BeautifulSoup
import re
import os
import configparser

parser = configparser.ConfigParser()
parser.read("config.txt")

session = HTMLSession()

pattern = r'https:\/\/(.*)\.com\.tr'

dir = parser.get("directory", "dir")
based_html_dir = parser.get("directory", "based_html_dir")

with open('site_list.json', "r") as json_file:
    data = json.load(json_file)

for site in data["site"]:
    r = session.get(site)
    # req = requests.get(site)
    soup = BeautifulSoup(r.text, features="lxml")    
    full_html = soup.prettify()
    filename = re.search(pattern, site)
    text_file = open(f"{filename.group(1)}_baseHTML.txt", "w" , encoding="utf-8")
    n = text_file.write(full_html)
    text_file.close()
    # os.replace(f'{dir}{filename.group(1)}_baseHTML.txt', f'{dir}{based_html_dir}')
    os.replace(f'{dir}{filename.group(1)}_baseHTML.txt', f'{dir}{based_html_dir}/{filename.group(1)}_baseHTML.txt')
    print(f'{filename.group(1)} base image tasindi')




