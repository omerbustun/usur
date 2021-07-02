from selenium import webdriver
import time
import datetime
import json
import re
import os
from skimage.metrics import structural_similarity as ssim
import imutils
import cv2
import configparser

parser = configparser.ConfigParser()
parser.read("config.txt")


dir = parser.get("directory", "dir")
archive_dir = parser.get("directory", "archive_dir")
nowTime = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M') # Now

if not os.path.exists(dir + f'{archive_dir}/' + nowTime):
    os.mkdir(dir + f'{archive_dir}/' + nowTime)
    print(f'New archive folder is created for {nowTime}')
else:
    print('Folder already exists')

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
    driver.save_screenshot((filename.group(1) + '.png'))

    # load the two input images
    imageA = cv2.imread('based_images/' + filename.group(1) + '_base.png')
    imageB = cv2.imread(filename.group(1) + '.png')
    # convert the images to grayscale
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    # compute the Structural Similarity Index (SSIM) between the two
    # images, ensuring that the difference image is returned
    (score, diff) = ssim(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    print("SSIM: {}".format(score))

    # threshold the difference image, followed by finding contours to
    # obtain the regions of the two input images that differ
    thresh = cv2.threshold(diff, 0, 255,
        cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    # loop over the contours
    for c in cnts:
        # compute the bounding box of the contour and then draw the
        # bounding box on both input images to represent where the two
        # images differ
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
    
    # show the output images
    
    if score <= 0.998: 
        print("Abi hacklendik galiba.")
        cv2.imshow("Original", imageA)
        cv2.imshow("Modified", imageB)
        cv2.waitKey(0)
         
    os.replace(f'/{(filename.group(1))}.png', f'{dir,archive_dir}')

driver.close()



