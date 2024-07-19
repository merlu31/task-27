from selenium.webdriver.common.by import By

from utils.WebUtilities import WebUtilities


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.web_util = WebUtilities(driver)
        self.USERNAME_FIELD = (By.XPATH, "//input[@name='username']")
        self.PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
        self.LOGIN_BUTTON = (By.XPATH, "//button[contains(.,'Login')]")
        self.FORGOT_PASSWORD_LINK = (By.XPATH, "//p[contains(.,'Forgot your password?')]")
        self.RESET_PASSWORD_BUTTON = (By.XPATH, "//button[contains(.,'Reset Password')]")
        self.SUCCESS_MESSAGE = (By.XPATH,
                                "//h6[@class='oxd-text oxd-text--h6 orangehrm-forgot-password-title'][contains(.,'Reset Password link sent successfully')]")

    def open_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.web_util.send_keys_to_element(self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.web_util.send_keys_to_element(self.PASSWORD_FIELD, password)

    def click_login_button(self):
        self.web_util.click_element(self.LOGIN_BUTTON)

    def get_error_message(self):
        ERROR_MESSAGE = (By.XPATH, "//p[contains(.,'Invalid credentials')]")
        return self.web_util.get_text_from_element(ERROR_MESSAGE)

    def click_forgot_password_link(self):
        self.web_util.click_element(self.FORGOT_PASSWORD_LINK)

    def click_reset_password_button(self):
        self.web_util.click_element(self.RESET_PASSWORD_BUTTON)

    def get_success_message(self):
        try:
            success_message_text = self.web_util.get_text_from_element(self.SUCCESS_MESSAGE)
            return success_message_text
        except Exception as e:
            print(f"Could not find the success message: {e}")
            return None
