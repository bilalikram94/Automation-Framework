from base.selenium_drivers import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time


class LoginPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    # Locators
    _login_link = "Login"  # By Link-Text
    _email_field = "user_email"  # By Name
    _password_field = "user_password"  # By Name
    _login_button = "commit"  # By Name
    _login_success = "//input[@id='search-courses']"  # By Xpath
    _failed_login = ".alert-danger"  # By CSS Selector
    _user_settings = "/html//div[@id='navbar']//ul[@class='nav navbar-nav navbar-right']/li[@class='dropdown']/a"  # Xpath
    _logout = "[href='\/sign_out']"  # By CSS Selector
    _logout_success = ".btn-primary.text-center"  # By CSS Selector

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")

    def login(self, email="", password=""):
        self.clickLoginLink()
        # self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent(self._login_success, locatorType="xpath")
        return result

    # def clearFields(self):
    #     emailField = self.getElement(locator=self._email_field)
    #     emailField.clear()
    #     passwordField = self.getElement(locator=self._password_field)
    #     passwordField.clear()

    def verifyLoginFailed(self):
        result = self.isElementPresent(self._failed_login, locatorType="css")
        return result

    def verifyTitle(self):

        if "Osama Anwar" in self.getTitle():
            return True
        else:
            return False

    def clickUserSettings(self):
        self.elementClick(self._user_settings, locatorType="xpath")

    def clickLogOut(self):
        self.elementClick(self._logout, locatorType="css")

    def verifySuccessfulLogout(self):
        result = self.isElementPresent(self._logout_success, locatorType="css")
        return result

    def Logout(self):
        self.clickUserSettings()
        time.sleep(2)
        self.clickLogOut()
