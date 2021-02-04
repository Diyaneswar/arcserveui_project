import pytest
import time
from selenium import webdriver
from pageObjects.loginpageobject import Loginpageclass
from utilities.loggenerator_utility import Logclass
from utilities.readProperties_utiity import Getconfigfiles
from utilities import excelfile_utility

class Test_tcid002_ddtlogin():
    
    baseURL = Getconfigfiles.getbaseURL()
    logger = Logclass.log_gen()
    path = r"C:\Users\Administrator\arcserveui_project\TestData\Book1.xlsx"
    
    def test_ddtlogin(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Loginpageclass(self.driver)
        self.row=excelfile_utility.getrowcount(self.path,"Sheet1")

        self.ddt_status = [] # empty list
        for r in range(2,self.row+1):# as it does not take the last row adding +1
            self.user = excelfile_utility.readrow(filepath=self.path, sheetname="Sheet1",r_num=r,c_num=1)
            self.password = excelfile_utility.readrow(filepath=self.path, sheetname="Sheet1",r_num=r,c_num=2)
            self.exp = excelfile_utility.readrow(filepath=self.path,sheetname='Sheet1',r_num=r,c_num=3)

            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clicklogin()
            time.sleep(5)

            self.exp_title = "Arcserve Business Continuity Cloud"
            self.act_title = self.driver.title

            if self.act_title == self.exp_title:
                if self.exp == 'pass':
                    self.logger.info("test case passed")
                    self.ddt_status.append("pass")
                elif self.exp == "fail":
                    self.logger.info("test case failed")
                    self.ddt_status.append("fail")

            elif self.act_title!= self.exp_title:
                if self.exp == 'pass':
                    self.logger.info("test case failed")
                    self.ddt_status.append("fail")
                elif self.exp == "fail":
                    self.logger.info("test case passed")
                    self.ddt_status.append("pass")

        if "fail" not in self.ddt_status:
            self.logger.info("-----DDT test case for loginscenarios passed------")
        else:
            self.logger.info("---------DDT test case failed----")






       
        