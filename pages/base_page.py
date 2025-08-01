import logging

class BasePage:
    def __init__(self, driver):
        logging.info("Driver is initializing...")
        self.driver = driver