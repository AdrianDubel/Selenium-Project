from selenium.webdriver.common.keys import Keys

class AddressPage:

    def __init__(self, driver):
        self.driver = driver

        self.addresses_btn_css = "[data-test='addresses']"
        self.new_address_xpath = "//a[.='New Address']"
        self.firstname_input_css = "#address_first_name"
        self.lastname_input_css = "#address_last_name"
        self.firstaddress_input_css = "#address_street_address"
        self.secondaddress_input_css = "#address_secondary_address"
        self.city_input_css = "#address_city"
        self.state_drop_css = "#address_state"
        self.zip_code_css = "#address_zip_code"
        self.age_input_css = "#address_age"
        self.phone_input_css = "#address_phone"
        self.climbing_check_css = "#address_interest_climb"
        self.submit_address_xpath = "//input[@name='commit']"
        self.alert_css = ".alert"

    def click_address(self):
        self.driver.find_element_by_css_selector(self.addresses_btn_css).click()

    def add_new_address(self):
        self.driver.find_element_by_xpath(self.new_address_xpath).click()

    def enter_first_name(self, name):
        self.driver.find_element_by_css_selector(self.firstname_input_css).send_keys(name)

    def enter_last_name(self, lastname):
        self.driver.find_element_by_css_selector(self.lastname_input_css).send_keys(lastname)

    def first_address(self, firstaddress):
        self.driver.find_element_by_css_selector(self.firstaddress_input_css).send_keys(firstaddress)

    def second_address(self, secondaddress):
        self.driver.find_element_by_css_selector(self.secondaddress_input_css).send_keys(secondaddress)

    def enter_city(self, city):
        self.driver.find_element_by_css_selector(self.city_input_css).send_keys(city)

    def state(self, state):
        drop = self.driver.find_element_by_css_selector(self.state_drop_css)
        drop.click()
        drop.send_keys(state)
        drop.send_keys(Keys.ENTER)

    def enter_zipcode(self, zipcode):
        self.driver.find_element_by_css_selector(self.zip_code_css).send_keys(zipcode)

    def enter_age(self, age):
        self.driver.find_element_by_css_selector(self.age_input_css).send_keys(age)

    def enter_phone(self, number):
        self.driver.find_element_by_css_selector(self.phone_input_css).send_keys(number)

    def climbing(self):
        self.driver.find_element_by_css_selector(self.climbing_check_css).click()

    def submit(self):
        self.driver.find_element_by_xpath(self.submit_address_xpath).click()

    def verify_alert(self):
        alert = self.driver.find_element_by_css_selector(self.alert_css)
        alert_visible = alert.is_displayed()
        alert_text = alert.text
        assert alert_visible == True
        assert alert_text == "Address was successfully created."

