import unittest
from appium import webdriver
import time

from appium.webdriver.common.touch_action import TouchAction


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
        
        self.driver.find_element_by_id("io.selendroid.testapp:id/touchTest").click()
        self.driver.find_element_by_id("io.selendroid.testapp:id/canvas_button").click()
		
        el = self.driver.find_element_by_id("io.selendroid.testapp:id/finger_view")
		
        actions = TouchAction(self.driver)
        actions.press(el, 300, 500)
        actions.move_to(el, 300, 800)
        actions.move_to(el, 600, 800)
        actions.move_to(el, 600, 500)
        actions.move_to(el, 300, 500)
        actions.move_to(el, 450, 300)
        actions.move_to(el, 750, 300)
        actions.move_to(el, 750, 600)
        actions.move_to(el, 600, 800)
        actions.move_to(el, 600, 500)
        actions.move_to(el, 750, 300)
        actions.wait(10000)
        actions.release()
        actions.perform()
        
    
    def tearDown(self):
        time.sleep(3)
        self.driver.quit()
	


if __name__ == '__main__':
    unittest.main()