import time
import pytest
import unittest
from utilities.teststatus import Status
from pages.home.login_page import LoginPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = Status(self.driver)

        """
        Need to verify two verification points
        1 fails, code will not go to the next verification point
        If assert fails, it stops current test execution and moves to the next test method.
        """

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verifyTitle()
        self.ts.mark(result1, "Title Verified")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "Login was successful")

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        time.sleep(3)
        self.lp.login("test@email.com", "abcabcabc")
        result = self.lp.verifyLoginFailed()
        self.ts.markFinal("test_invalidLogin", result, "Login wasn't successful")

    @pytest.mark.run(order=3)
    def test_validlogout(self):
        self.lp.Logout()
        result = self.lp.verifySuccessfulLogout()
        self.ts.markFinal("test_validLogout", result, "Logout successful")
