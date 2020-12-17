from pytest_bdd import given, when, then, parsers

from tests.step_defs.common_locators import CommonLocators


#steps


@given('Login modal is open')
def open_login_modal(browser):
    browser.open("https://www.boardinfinity.com/")
    browser.wait_for_element_displayed(CommonLocators.signin_button)
    browser.mouse_hover(CommonLocators.signin_button)
    browser.not_visible_click(CommonLocators.signin_button)
    browser.wait_for_element_displayed(CommonLocators.login_username)
    pass
