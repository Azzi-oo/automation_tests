from pages.base import BasePage
from selenium.webdriver.common.by import By
import allure

button_selector = (By.LINK_TEXT, 'Click')
result_selector = (By.ID, 'result-text')


class LikedButtonPage(BasePage):
    def __init__(self, browser) -> None:
        super().__init__(browser)


    @property
    def button(self):
        return self.find(button_selector)

    def open(self):
        with allure.step('Open like a button page'):
            self.browser.get('https://www.qa-practice.com/elements/button/like_a_button')

    def result(self):
        return self.find(result_selector)


    @property
    def button_is_displayed(self):
        with allure.step('Check that button is displayed'):
            return self.button_is_displayed()

    def button_click(self):
        with allure.step('Click the button'):
            self.button_click()


    @property
    def result(self):
        return self.find(result_selector)


    @property
    def result_text(self):
        with allure.step('Get result text'):
            return self.result.text
