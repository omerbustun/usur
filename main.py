from selenium import webdriver
import time
import json
import re
from PIL import Image
from pathlib import Path

driver = webdriver.Chrome()

with open('site_list.json', "r") as json_file:
    data = json.load(json_file)

pattern = r'https:\/\/(.*)\.com\.tr'

cwd = Path.cwd()
mod_path = Path(__file__).parent
rel_path = 'yeni/'

for site in data["site"]:
    driver.maximize_window()
    driver.get(site)
    driver.refresh()
    print (site)
    print(type(site))
    time.sleep(3)
    filename = re.search(pattern, site)
    print (filename.group(1))
    print (filename)
    driver.save_screenshot((filename.group(1) + '.png'))

driver.close()