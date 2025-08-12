from behave import *
from pages.homePage import HomePage

    
@Given('I go to homepage')
def step_impl(context):
    context.home_page.goToHomePage()

@When('I click Alerts, Frame & Windows')
def step_impl(context):
    context.home_page.clickElementHeader()

@Then('I check message after redirection')
def step_impl(context):
    context.home_page.checkMessage()  