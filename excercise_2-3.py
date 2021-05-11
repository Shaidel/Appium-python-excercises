import unittest
from appium import webdriver
import time

import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class AppiumTest(unittest.TestCase):
    dc = {}
    driver = None
	
    def setUp(self):
        
        self.dc['automationName'] = "Appium"
        self.dc['platformName'] = "Android"
        self.dc['deviceName'] = "emulator-5554"
        self.dc['appPackage'] = "io.selendroid.testapp"
        self.dc['appActivity'] = "io.selendroid.testapp.HomeScreenActivity"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.dc)

    def testTouchActions(self):
        self.driver.implicitly_wait(30)
        
        self.driver.find_element_by_id("io.selendroid.testapp:id/showToastButton").click()
        
        time.sleep(10)		
        self.driver.get_screenshot_as_file("test.png")
        time.sleep(10)  
    
    def tearDown(self):
        time.sleep(3)
        self.driver.quit()
	

if __name__ == '__main__':
    unittest.main()