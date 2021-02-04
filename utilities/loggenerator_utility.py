import logging

class Logclass():
    @staticmethod
    def log_gen():
        logging.basicConfig(filename=r"C:\Users\Administrator\arcserveui_project\Logs\automation.log",format='%(levelname)s:%(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        
        return logger