import configparser

config = configparser.RawConfigParser()
config.read(r"C:\Users\Administrator\arcserveui_project\Configurations\config.ini")

class Getconfigfiles():
    #creating 3 methods for 3 variables present in the init file
    @staticmethod
    def getbaseURL():
        url = config.get('setupinfo','baseURL')
        return url

    @staticmethod
    def getusername():
        username=config.get('setupinfo','username')
        return username

    @staticmethod
    def getpassword():
        password=config.get('setupinfo','password')
        return password





