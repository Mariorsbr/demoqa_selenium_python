from selenium.webdriver.common.by import By

class BrowserWidowPage:
    def __init__(self,driver):
        self.driver = driver
        self.alert_frame_windows = driver.find_element(By.Xpath,'//*[@id="item-1" and contains(normalize-space(.), "Browser Windows")]')



    def goToBrowserWindows(self):
        self.alert_frame_windows.click()
