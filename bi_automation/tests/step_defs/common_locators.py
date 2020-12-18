from selenium.webdriver.common.by import By


class CommonLocators:
    login_username = (By.CSS_SELECTOR, "#login-form_id")
    login_password = (By.CSS_SELECTOR, "#login-form_password")
    signin_button = (By.XPATH, "//*[@id='__next']/div/div[1]/div[2]/div[1]/button")