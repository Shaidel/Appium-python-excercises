import unittest
from appium import webdriver
import time

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class AppiumTest(unittest.TestCase):
    dc = {}
    driver = None
	
    def setUp(self):
        
        self.dc['automationName'] = "Appium"
        self.dc['platformName'] = "Android"
        self.dc['deviceName'] = "emulator-5554"
        self.dc['appPackage'] = "com.everydaycalculation.casiocalculator"
        self.dc['appActivity'] = "com.everydaycalculation.casiocalculator.Basic"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.dc)
		
    def testCalcAddition(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id("com.everydaycalculation.casiocalculator:id/btn_2").click()	
        self.driver.find_element_by_id("com.everydaycalculation.casiocalculator:id/btn_add").click()
        self.driver.find_element_by_id("com.everydaycalculation.casiocalculator:id/btn_2").click()
        self.driver.find_element_by_id("com.everydaycalculation.casiocalculator:id/btn_equals").click()
        time.sleep(3)		
        self.driver.get_screenshot_as_file("CalcAdd.png")        
        textCalcAdd = pytesseract.image_to_string("CalcAdd.png")
        #print (textCalcAdd)
		
        logCalcAdd = open(r'logCalcAdd.txt','w')
        logCalcAdd.write(textCalcAdd)
        logCalcAdd.close()
				
        if "GT =\n\n4" in textCalcAdd:
            print ("Yes, 2 plus 2 equals 4")
            print ("Test 1 OK")
        else:
            print ("Better get an abacus")
            print ("Test 1 FAIL")

    def testCalcSubtraction(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id("com.everydaycalculation.casiocalculator:id/btn_7").click()	
        self.driver.find_element_by_id("com.everydaycalculation.casiocalculator:id/btn_subtract").click()
        self.driver.find_element_by_id("com.everydaycalculation.casiocalculator:id/btn_4").click()
        self.driver.find_element_by_id("com.everydaycalculation.casiocalculator:id/btn_equals").click()
        time.sleep(3)		
        self.driver.get_screenshot_as_file("CalcSub.png")        
        textCalcSub = pytesseract.image_to_string("CalcSub.png")
        #print (textCalcSub)
		
        logCalcSub = open(r'logCalcSub.txt','w')
        logCalcSub.write(textCalcSub)
        logCalcSub.close()		
		
        if "GT =\n\n3" in textCalcSub:
            print ("Yes, 7 minus 4 equals 3")
            print ("Test 2 OK")
        else:
            print ("Better get an abacus")
            print ("Test 2 FAIL")
			
    def testCalcMultiplication(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id("com.everydaycalculation.casiocalculator:id/btn_7").click()	
        self.driver.find_element_by_id("com.everydaycalculation.casiocalculator:id/btn_multiply").click()
        self.driver.find_element_by_id("com.everydaycalculation.casiocalculator:id/btn_3").click()
        self.driver.find_element_by_id("com.everydaycalculation.casiocalculator:id/btn_equals").click()
        time.sleep(3)		
        self.driver.get_screenshot_as_file("CalcMult.png")        
        textCalcMult = pytesseract.image_to_string("CalcMult.png")
        #print (textCalcMult)
		
        logCalcMult = open(r'logCalcMult.txt','w')
        logCalcMult.write(textCalcMult)
        logCalcMult.close()		
		
        if "GT =\n\n21" in textCalcMult:
            print ("Yes, 7 multiply 3 equals 21")
            print ("Test 3 OK")
        else:
            print ("Better get an abacus")
            print ("Test 3 FAIL")
			
    def testCalcDivision(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id("com.everydaycalculation.casiocalculator:id/btn_9").click()	
        self.driver.find_element_by_id("com.everydaycalculation.casiocalculator:id/btn_divide").click()
        self.driver.find_element_by_id("com.everydaycalculation.casiocalculator:id/btn_3").click()
        self.driver.find_element_by_id("com.everydaycalculation.casiocalculator:id/btn_equals").click()
        time.sleep(3)		
        self.driver.get_screenshot_as_file("CalcDiv.png")        
        textCalcDiv = pytesseract.image_to_string("CalcDiv.png")
        #print (textCalcDiv)
		
        logCalcDiv = open(r'logCalcDiv.txt','w')
        logCalcDiv.write(textCalcDiv)
        logCalcDiv.close()		
		
        if "GT =\n\n3" in textCalcDiv:
            print ("Yes, 9 divide 3 equals 3")
            print ("Test 4 OK")
        else:
            print ("Better get an abacus")
            print ("Test 4 FAIL")
			
    def tearDown(self):
        time.sleep(3)
        self.driver.quit()
	

if __name__ == '__main__':
    unittest.main()