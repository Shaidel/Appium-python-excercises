import unittest
from appium import webdriver
import time


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

    def testUserRegistration(self):
        self.driver.implicitly_wait(30)
        
        self.driver.find_element_by_id("io.selendroid.testapp:id/startUserRegistration").click()
        self.driver.find_element_by_id("io.selendroid.testapp:id/inputUsername").send_keys("Andrzej")
        self.driver.find_element_by_id("io.selendroid.testapp:id/inputEmail").send_keys("andrzej@mail.com")
        self.driver.find_element_by_id("io.selendroid.testapp:id/inputPassword").send_keys("%seCRET%")
        self.driver.find_element_by_id("io.selendroid.testapp:id/inputName").clear()
        self.driver.find_element_by_id("io.selendroid.testapp:id/inputName").send_keys("Mr. Wonż")	
		
        self.driver.hide_keyboard()
        		
        self.driver.find_element_by_id("android:id/text1").click()	
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.ListView/android.widget.CheckedTextView[4]").click()
        self.driver.find_element_by_id("io.selendroid.testapp:id/input_adds").click()
        self.driver.find_element_by_id("io.selendroid.testapp:id/btnRegisterUser").click()
		
        nameText = self.driver.find_element_by_id("io.selendroid.testapp:id/label_name_data").get_attribute('name')
        print ("Name: " + nameText)
		
        usernameText = self.driver.find_element_by_id("io.selendroid.testapp:id/label_username_data").get_attribute('name')
        print ("Username: " + usernameText)
		
        passwordText = self.driver.find_element_by_id("io.selendroid.testapp:id/label_password_data").get_attribute('name')
        print ("Password: " + passwordText)
		
        emailText = self.driver.find_element_by_id("io.selendroid.testapp:id/label_email_data").get_attribute('name')
        print ("E-Mail: " + emailText)
		
        preferedProgrammingLanguageText = self.driver.find_element_by_id("io.selendroid.testapp:id/label_preferedProgrammingLanguage_data").get_attribute('name')
        print ("Programming Language: " + preferedProgrammingLanguageText)
		
        acceptAddsText = self.driver.find_element_by_id("io.selendroid.testapp:id/label_acceptAdds_data").get_attribute('name')
        print ("I accept adds: " + acceptAddsText)
		
        time.sleep(3)
        self.driver.find_element_by_id("io.selendroid.testapp:id/buttonRegisterUser").click()
    
    def tearDown(self):
        self.driver.quit()
	


if __name__ == '__main__':
    unittest.main()