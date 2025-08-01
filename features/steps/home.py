from behave import *
from drivers.browser import get_driver
from pages.homePage import HomePage

    
@Given('I open the demoqa home page')
def step_impl(context):
    context.driver = get_driver()
    home_page = HomePage(context.driver)
    home_page.goToHomePage()