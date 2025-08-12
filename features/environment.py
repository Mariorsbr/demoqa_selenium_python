from behave import fixture, use_fixture
# from behave4my_project.fixtures import wsgi_server
from selenium import webdriver
from pages.homePage import HomePage

@fixture
def selenium_browser_chrome(context):
    # -- HINT: @behave.fixture is similar to @contextlib.contextmanager
    context.browser = webdriver.Chrome()
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()

def before_all(context):
    # use_fixture(wsgi_server, context, port=8000)
    use_fixture(selenium_browser_chrome, context)
    # -- HINT: CLEANUP-FIXTURE is performed after after_all() hook is called.

def before_scenario(context, scenario):
    # código para rodar antes de cada cenário
    context.home_page = HomePage(context.browser)

# def before_feature(context, feature):
#     model.init(environment='test')