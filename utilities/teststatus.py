"""
    @packages utilities
    Checkpoint class implementation
    It provides functionality to assert result

Example:
        self.check_point.markFinal("Test Name" , result, "Message")
"""
from base.selenium_drivers import SeleniumDriver
import utilities.custom_logger as cl
import logging


class Status(SeleniumDriver):
    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        """
        Inits Checkpoint Class

        """
        super(Status, self).__init__(driver)

        self.resultList = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL :: + " + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.info("### VERIFICATION FAILED :: + " + resultMessage)


            else:
                self.resultList.append("FAIL")
                self.log.error("### VERIFICATION FAILED :: + " + resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.error("### EXCEPTION OCCURRED !!!")

    def mark(self, result, resultMessage):
        """
        Mark the result of the verification point in a test case
        """
        self.setResult(result, resultMessage)

    def markFinal(self, testName, result, resultMessage):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be the final test status of the test case
        """
        self.setResult(result, resultMessage)

        if "FAIL" in self.resultList:
            self.log.error(testName + "### Test Failed")
            self.resultList.clear()
            assert True == False

        else:
            self.log.info(testName + "### Test Successful")
            self.resultList.clear()
            assert True == True