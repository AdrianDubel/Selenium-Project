class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.home_btn_xpath = "//a[@href='/']"
        self.signin_btn_xpath = "//a[@id='sign-in']"
        self.email_input_css = "#session_email"
        self.password_input_css = "#session_password"
        self.submit_xpath = "//input[@name='commit']"
        self.signup_btn_css = "[data-test='sign-up']"
        self.reg_email_input_css = "#user_email"
        self.reg_password_input_css = "#user_password"
        self.title_css = "h1"
        self.alert_css = ".alert"

    def click_home(self):
        self.driver.find_element_by_xpath(self.home_btn_xpath).click()

    def click_signin(self):
        self.driver.find_element_by_xpath(self.signin_btn_xpath).click()

    def enter_email(self, email):
        self.driver.find_element_by_css_selector(self.email_input_css).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element_by_css_selector(self.password_input_css).send_keys(password)

    def click_submit(self):
        self.driver.find_element_by_xpath(self.submit_xpath).click()

    def click_signup(self):
        self.driver.find_element_by_css_selector(self.signup_btn_css).click()

    def enter_new_email(self, email):
        self.driver.find_element_by_css_selector(self.reg_email_input_css).send_keys(email)

    def enter_new_password(self, password):
        self.driver.find_element_by_css_selector(self.reg_password_input_css).send_keys(password)

    def check_header(self):
        title = self.driver.find_element_by_css_selector(self.title_css)
        title_text = title.text
        title_visible = title.is_displayed()
        assert title_text == "Welcome to Address Book"
        assert title_visible == True

    def check_alert(self):
        error = self.driver.find_element_by_css_selector(self.alert_css)
        error_text = error.text
        error_visible = error.is_displayed()
        assert error_text == "Bad email or password."
        assert error_visible == True

        