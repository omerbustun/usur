from selenium import webdriver
import time
import datetime
import json
import re
import os
from skimage.metrics import structural_similarity as ssim
import configparser

parser = configparser.ConfigParser()
parser.read("config.txt")


dir = parser.get("directory", "dir")
based_images_dir = parser.get("directory", "based_images_dir")

driver = webdriver.Chrome()

with open('site_list.json', "r") as json_file:
    data = json.load(json_file)

pattern = r'https:\/\/(.*)\.com\.tr'

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
    driver.save_screenshot((filename.group(1) + '_base.png'))
    os.replace(f'{dir}{filename.group(1)}_base.png', f'{dir}{based_images_dir}/{filename.group(1)}_base.png')
    print(f'{filename.group(1)} base image tasindi')

driver.close()