import time
import pytest
from pageObjects.loginpageobject import Loginpageclass
from utilities.readProperties_utiity import Getconfigfiles
from utilities.loggenerator_utility import Logclass

class Test_tcid001_login():

    baseURL = Getconfigfiles.getbaseURL()
    username = Getconfigfiles.getusername()
    password = Getconfigfiles.getpassword()

    logger=Logclass.log_gen()

    def test_homepagetitle(self,setup):
        self.logger.info("----------Test_tcid001_login----------")
        self.logger.info("----------validating homepagetitle------")
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title == "Arcserve Business Continuity Cloud":
            assert True
            self.logger.info("Home page title is validated successful")
            self.driver.close()
        else:
            self.logger.info("Home page title is validated failed")
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepage.png")
            self.driver.close()

    def test_loginwithvalidcred(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(5)
        self.lp = Loginpageclass(self.driver)
        self.lp.setUsername(username=self.username)
        self.lp.setPassword(password=self.password)
        self.lp.clicklogin()
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Arcserve Business Continuity Cloud":
            assert True
        else:
            assert False








