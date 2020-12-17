from selenium.webdriver import ActionChains
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, element_to_be_clickable, \
    text_to_be_present_in_element
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

DEFAULT_TIMEOUT = 30
LONG_DEFAULT_TIMEOUT = 60


class Browser:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def refresh(self):
        self.driver.refresh()

    def find_element(self, locator):
        by, expression = locator
        return self.driver.find_element(by, expression)

    def click(self, locator):
        return self.find_element(locator).click()

    def click_missed(self, locator):
        self.mouse_hover(locator)
        self.not_visible_click(locator)

    def not_visible_click(self, locator):
        ele = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", ele)

    def mouse_hover(self, locator):
        action = ActionChains(self.driver)
        element = self.find_element(locator)
        action.move_to_element(element)
        action.perform()

    def switch_back_to_first_window(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])

    def switch_to_new_window(self):
        new_window_position = len(self.driver.window_handles) - 1
        self.driver.switch_to.window(self.driver.window_handles[new_window_position])

    def switch_to_iframe(self, iframe, timeout=DEFAULT_TIMEOUT):
        self.wait_for_element_displayed(iframe, timeout)
        self.driver.switch_to.frame(self.find_element(iframe))

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def is_displayed(self):
        self.driver.is_displayed()

    def wait_for_element_displayed(self, locator, timeout=DEFAULT_TIMEOUT):
        if timeout != DEFAULT_TIMEOUT:
            webdriver_wait = WebDriverWait(self.driver, timeout)
        else:
            webdriver_wait = self.wait
        webdriver_wait.until(visibility_of_element_located(locator))

    def wait_for_element_not_displayed(self, locator, timeout=DEFAULT_TIMEOUT):
        if timeout != DEFAULT_TIMEOUT:
            webdriver_wait = WebDriverWait(self.driver, timeout)
        else:
            webdriver_wait = self.wait
        webdriver_wait.until_not(visibility_of_element_located(locator))

    def text_to_be_present_in_element(self, locator, value):
        self.wait.until(text_to_be_present_in_element(locator, value))

    def wait_for_element_to_be_clickable(self, locator):
        self.wait_for_element_displayed(locator)
        self.wait.until(element_to_be_clickable(locator))

    def type(self, locator, value):
        self.wait_for_element_displayed(locator)
        element = self.find_element(locator)
        element.send_keys(value)

    def text(self, locator):
        return self.find_element(locator).text

    def verify_text_on_page(self, locator, text):
        self.wait_for_element_displayed(locator)
        text_found = self.find_element(locator).text
        if text_found == text:
            return True
        else:
            raise Exception(CommonData.text_mismatch_at_location_exception(locator, text, text_found))

    def select_option_from_menu(self, locator, option):
        dropdown = Select(self.find_element(locator))
        dropdown.select_by_value(option)

    def select_option_from_menu_by_text(self, locator, option):
        dropdown = Select(self.find_element(locator))
        dropdown.select_by_visible_text(option)

    def verify_css_property(self, locator, css_attribute, expected_value):
        self.wait_for_element_displayed(locator)
        actual_value = self.find_element(locator).value_of_css_property(css_attribute)
        if actual_value == expected_value:
            return True
        else:
            raise Exception(
                CommonData.css_attribute_mismatch_at_location_exception(locator, css_attribute, expected_value,
                                                                        actual_value))
