from base.selenium_drivers import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time


class AllCourses(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)
    # Locator
    _all_courses = "//div[@id='navbar']//ul[@class='nav navbar-nav navbar-right']//a[@href='/courses']"  # Xpath
    _course = "//div[@class='course-listing-title'][contains(text(),'Selenium WebDriver With Java')]"  # Xpath
    _verify_course = "//div[@class='view-school']/div/div[1]/div[@class='course-top-row has-hero-image']//h1[@class='course-title']"  # Xpath
    _verify_all_course = "//input[@id='search-courses']"  # By Xpath

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def clickAllCourseLink(self):
        self.elementClick(self._all_courses, locatorType="xpath")

    def verifyAllCourse(self):
        result = self.isElementPresent(self._verify_all_course, locatorType="xpath")
        return result

    def clickCourseLink(self):
        self.elementClick(self._course, locatorType="xpath")

    def verifyCourse(self):
        result = self.isElementPresent(self._verify_course, locatorType="xpath")
        return result







