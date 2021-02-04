import time
from pageObjects.addsource_pageobjects import Addsrc_pageobjects
from pageObjects.loginpageobject import Loginpageclass
from utilities.loggenerator_utility import Logclass
from utilities.readProperties_utiity import Getconfigfiles

class Test_tcid003_addsrc():

    baseURL = Getconfigfiles.getbaseURL()
    logger =Logclass.log_gen()
    username=Getconfigfiles.getusername()
    password=Getconfigfiles.getpassword()

    def test_addwinsrc(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp=Loginpageclass(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        time.sleep(5)
        self.ad=Addsrc_pageobjects(self.driver)
        self.ad.btn_protect_menu()
        self.ad.btn_addsrc_menu()
        self.ad.drp_addwin()
        time.sleep(3)
        self.ad.btn_selsite()
        self.ad.drp_hpsite()
        self.ad.txt_srcname("172.30.54.173")
        self.ad.txt_usrname("administrator")
        self.ad.txt_pwd("Msys#123")
        self.btn_addwin()







