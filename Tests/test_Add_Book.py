from selenium import webdriver
import unittest
from Pages.Addresses_Page import AddressPage
from Pages.Home_Page import HomePage
from faker import Faker
from time import sleep

class AddAddressTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_add_address(self):
        driver = self.driver

        url = "http://a.testaddressbook.com/sign_in"
        email = "test@wp.pl"
        password = "12345678"
        faker = Faker()
        firstname = faker.first_name()
        lastname = faker.last_name()
        address1 = "Street Avenue"
        address2 = "23"
        city = "Los Angeles"
        state = "ke"
        age = "27"
        zip = faker.zipcode()
        phone = "222333444"

        driver.get(url)
        home_page = HomePage(driver)
        home_page.enter_email(email)
        home_page.enter_password(password)
        home_page.click_submit()

        address_page = AddressPage(driver)
        address_page.click_address()
        address_page.add_new_address()
        address_page.enter_first_name(firstname)
        address_page.enter_last_name(lastname)
        address_page.first_address(address1)
        address_page.second_address(address2)
        address_page.enter_city(city)
        address_page.state(state)
        address_page.enter_zipcode(zip)
        address_page.enter_age(age)
        address_page.enter_phone(phone)
        address_page.submit()
        address_page.verify_alert()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
