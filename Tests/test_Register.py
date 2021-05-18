from selenium import webdriver
from time import sleep
import unittest
from Pages.Home_Page import HomePage
from faker import Faker
from time import sleep



class RegisterTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_register(self):
        driver = self.driver

        url = "http://a.testaddressbook.com/sign_in"
        faker = Faker()
        email = faker.company_email()
        password = "12345678"

        driver.get(url)
        home_page = HomePage(driver)
        home_page.click_signup()
        home_page.enter_new_email(email)
        home_page.enter_new_password(password)
        home_page.click_submit()
        home_page.check_header()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()



