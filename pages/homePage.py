from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    alert_frame_windows = (By.XPATH,'//h5[text() = "Alerts, Frame & Windows"]')
    message = (By.XPATH,'//div[text()="Please select an item from left to start practice."]')

    def __init__(self, browser):
        super().__init__(browser)

    def goToHomePage(self):
         self.browser.get('https://demoqa.com/')  

    def clickElementHeader(self):
        self.click(self.alert_frame_windows)

    def checkMessage(self):
        try:
            self.wait_for_element_visible
        except:
            raise AssertionError("Element is not visible on the page")             