from selenium import webdriver
import time
#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then
#invoke actual browser
driver = webdriver.Chrome()
# to maximize the browser window
driver.maximize_window()
#get method to launch the URL
driver.get("https://eksim.com.tr")
#to refresh the browser
driver.refresh()
#to get the screenshot of complete page
time.sleep(3)
driver.save_screenshot("screenshot_tutorialspoint.png")
#to close the browser
driver.close()