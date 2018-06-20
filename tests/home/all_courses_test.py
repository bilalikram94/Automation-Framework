import unittest
import time
import pytest

from pages.home.login_page import LoginPage
from pages.home.all_courses import AllCourses
from utilities.teststatus import Test


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class AllCoursesTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def ClassSetUp(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ac = AllCourses(self.driver)
        self.lp.login("test@email.com", "abcabc")
        time.sleep(3)

    @pytest.mark.run(order=1)
    def test_course(self):
        self.ac.clickAllCourseLink()
        time.sleep(3)
        result1 = self.ac.verifyAllCourse()
        assert result1 == True
        time.sleep(3)
        self.ac.clickCourseLink()
        result = self.ac.verifyCourse()
        assert result == True
        self.lp.Logout()
        result2 = self.lp.verifySuccessfulLogout()
        assert result2 == True

    #@pytest.mark.run(order=2)
    #def test_logout(self):
    #    time.sleep(2)
    #    self.lp.Logout()
    #    result = self.lp.verifySuccessfulLogout()
    #    assert result == True

