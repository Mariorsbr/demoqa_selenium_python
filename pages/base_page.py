import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BasePage:
    def __init__(self,browser, timeout=10):
        logging.info("Driver is initializing...")
        self.browser = browser
        self.wait = WebDriverWait(browser, timeout)
        
    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def click(self, locator):
        element = self.wait_for_element_visible(locator)
        element.click()        
        time.sleep(2) 