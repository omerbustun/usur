from selenium import webdriver
import selenium
import sys, os
import time
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()
chrome_options = Options()
chrome_options.add_argument("--headless")


URL = 'https://eksim.com.tr'
driver.get(URL)
time.sleep(3)
#driver.save_screenshot('ss{0}.png'.format(URL))
driver.save_screenshot('test.png')

driver.quit()

