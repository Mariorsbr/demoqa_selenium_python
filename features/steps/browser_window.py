from behave import *
from drivers.browser import get_driver
from pages.browserWindowPage import BrowserWidowPage

    
@Given('I go to the Browser Windows page through Alerts, Frame & Windows menu')
def step_impl(context):
    driver = get_driver()
    browser_window = BrowserWidowPage(driver)
    browser_window.goToBrowserWindows()