from selenium.webdriver.common.by import By

class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.forms_option = driver.find_element(By.CSS_SELECTOR, "card-body")
        self.first_name = driver.find_element(By.CSS_SELECTOR, "#firstName")

    def submit_form(self, name):
        self.driver.get("https://demoqa.com/automation-practice-form")
        self.first_name.send_keys(name)    

       
