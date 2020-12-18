from pytest_bdd import given, when, parsers
from selenium.webdriver.common.keys import Keys
import time

from tests.step_defs.common_locators import CommonLocators
from tests.step_defs.login.login_data import LoginData


# steps


@given('Login modal is open')
def open_login_modal(browser):
    browser.open("https://www.boardinfinity.com/")
    browser.wait_for_element_displayed(CommonLocators.signin_button)
    browser.mouse_hover(CommonLocators.signin_button)
    browser.click(CommonLocators.signin_button)
    time.sleep(10)
    browser.wait_for_element_displayed(CommonLocators.login_username)
    pass


@when(parsers.parse('Login with "{username}"'))
def enter_credentials(browser, username):
    enter_username_and_submit(browser, username)
    enter_password_and_submit(browser, LoginData.default_password)


def enter_username_and_submit(browser, username):
    browser.wait_for_element_displayed(CommonLocators.login_username)
    browser.type(CommonLocators.login_username, username + Keys.RETURN)


def enter_password_and_submit(browser, password):
    browser.wait_for_element_displayed(CommonLocators.login_password)
    browser.type(CommonLocators.login_password, password + Keys.RETURN)
