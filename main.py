from selenium import webdriver
import time
import json
import sys

driver = webdriver.Chrome()

with open('site_list.json', "r") as json_file:
    data = json.load(json_file)

for site in data["site"]:
    #driver.maximize_window()
    driver.get(site)
    driver.refresh()
    print (site)
    print(type(site))
    time.sleep(3)
    filename = "%s" % site
    print (filename)
    driver.save_screenshot(f"{filename}.png")



driver.close()