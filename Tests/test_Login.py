from selenium import webdriver
from time import sleep
import unittest
from Pages.Home_Page import HomePage

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver

        url = "http://a.testaddressbook.com/sign_in"
        email = "test@wp.pl"
        password = "12345678"

        driver.get(url)
        home_page = HomePage(driver)
        home_page.enter_email(email)
        home_page.enter_password(password)
        home_page.click_submit()
        home_page.check_header()

    def test_login_invalid(self):
        driver = self.driver

        url = "http://a.testaddressbook.com/sign_in"
        email = "test_wrong@wp.pl"
        password = "12345678"

        driver.get(url)
        home_page = HomePage(driver)
        home_page.enter_email(email)
        home_page.enter_password(password)
        home_page.click_submit()
        home_page.check_alert()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()




