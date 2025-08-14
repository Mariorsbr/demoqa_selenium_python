from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class BrowserWidowPage(BasePage):
    browser_windows = (By.XPATH,"//*['span.text'][text()= 'Browser Windows')]") 

    def __init__(self, browser):
        super().__init__(browser)


    def goToBrowserWindows(self):
        self.click(self.browser_windows)
