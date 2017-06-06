#!/usr/bin/env python
"""
@name:slither_circle_bot.py - Slither.io Bots for Python
@disclaimer:Copyright 2017, KRIPT4
@lastrelease: Jun 6 2017
More info:
 * KRIPT4: https://github.com/KRIPT4/Slither.io-Bots-for-Python
"""

import sys
import math
import time
import pyautogui
# Import the Selenium 2 module (aka "webdriver")
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument('--enable-precise-memory-info')
chrome_options.add_argument('--ignore-ssl-errors=true --debug=true')
chrome_options.add_argument('--start-fullscreen')
chrome_options.add_experimental_option('prefs', {
    'credentials_enable_service': False,
    'profile': {
        'password_manager_enabled': False
    }
})
global driver

def main():

	global driver
	driver  = webdriver.Chrome(executable_path = 'chromedriver.exe', chrome_options = chrome_options)
	varUSER = 'Bot for Python'

	driver.get('http://slither.io/')
	time.sleep(1)

	retryElement('//*[@id="nick"]').send_keys(varUSER)
	retryElement('//*[@id="playh"]/div/div/div[3]').click()
	time.sleep(2)
 
	x, y = pyautogui.size()
	centerXStr = int(x) / 2
	centerYStr = int(y) / 2
	pyautogui.moveTo(int(centerXStr),int(centerYStr),duration=0.25)
	positionXStr = round(int(centerXStr) / 2 + int(centerXStr))
	pyautogui.moveTo(int(positionXStr),int(centerYStr),duration=0.25)

	radio = 300
	g = 0

	for g in range(300):
		x = int(math.cos(g) * radio + int(centerXStr))
		y = int(math.sin(g) * radio + int(centerYStr))
		g += 0.1
		pyautogui.moveTo(int(x),int(y),duration=0.16)

	pyautogui.moveTo(int(centerXStr),int(centerYStr))

def retryElement(xpath):
	for i in range(0,50):
		try:
			element = driver.find_element_by_xpath(xpath)
			return element
		except Exception as e:
			time.sleep(0.1)
			continue
	brikear(("Error XPATH: %s" % xpath))

def brikear(msg):
	print(msg)
	closeDriver()
	sys.exit(1)

def closeDriver():
	global driver
	driver.quit()

try:
	main()
except Exception as e:
	print(e)
	closeDriver()