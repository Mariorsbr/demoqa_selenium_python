from behave import *
from pages.homePage import HomePage

    
@Given('I go to homepage')
def step_impl(context):
    context.home_page.goToHomePage()

@When('I click {header}')
def step_impl(context, header):
    locators = {
        "Elements": context.home_page.elementsHeader,
        "Forms": context.home_page.formsHeader,
        "Alerts, Frame & Windows": context.home_page.alertFramesWindowsHeader,
        "Widgets": context.home_page.widgetsHeader,
        "Interactions": context.home_page.interactionsHeader,
        "Book Store Application": context.home_page.bookStoreApplicationHeader,
    }
    context.home_page.clickElementHeader(locators.get(header))

@Then('I check message after redirection')
def step_impl(context):
    context.home_page.checkMessage()  