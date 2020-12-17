#import allure
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from tests.step_defs.framework.browser import Browser

caps = {}


# Fixtures


# @pytest.fixture
# def env(request):
#     return request.config.getoption("--env")


@pytest.fixture
def browser_name(request):
    return request.config.getoption("--browser")


@pytest.fixture
def driver(browser_name, request):
    # if browser_name == 'grid_chrome':
    #     caps['browserName'] = 'chrome'
    #     d = webdriver.Remote(command_executor=CommonData.remote_url, desired_capabilities=caps)
    if browser_name == 'chrome':
        d = webdriver.Chrome()
    d.set_window_size(1500, 900)
    yield d

    # Do teardown (this code will be executed after each test):

    # if request.node.rep_call.failed:
    #     # Make the screen-shot if test failed:
    #     try:
    #         allure.attach(d.current_url,
    #                       name='url',
    #                       attachment_type=allure.attachment_type.TEXT)
    #         allure.attach(d.get_screenshot_as_png(),
    #                       name='Screenshot',
    #                       attachment_type=allure.attachment_type.PNG)
    #     except:
    #         print('screenshot could not be captured')  # just ignore
    d.quit()


@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, 10)
    return wait


@pytest.fixture
def browser(driver):
    b = Browser(driver)
    return b
