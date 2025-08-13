from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class HomePage(BasePage):
    elementsHeader = (By.XPATH,'//h5[contains(text(),"Elements")]')
    formsHeader = (By.XPATH,'//h5[contains(text(), "Forms")]')
    alertFramesWindowsHeader = (By.XPATH,'//h5[contains(text(), "Alerts, Frame & Windows")]')
    widgetsHeader = (By.XPATH,'//h5[contains(text(), "Widgets")]')
    interactionsHeader = (By.XPATH,'//h5[contains(text(), "Interactions")]')
    bookStoreApplicationHeader = (By.XPATH,'//h5[contains(text(), "Book Store Application")]')
    message = (By.XPATH,'//div[text()="Please select an item from left to start practice."]')

    def __init__(self, browser):
        super().__init__(browser)

    def goToHomePage(self):
         self.browser.get('https://demoqa.com/')  

    def clickElementHeader(self, locator):
        self.click(locator)
        time.sleep(1)

    def checkMessage(self):
        try:
            self.wait_for_element_visible(self.message)
        except:
            raise AssertionError("Element is not visible on the page")             