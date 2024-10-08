from pages.base import BasePage
from selenium.webdriver.common.by import By


button_selector = (By.ID, 'submit-id-submit')
result_selector = (By.ID, 'result-text')


class SimpleButtonPage(BasePage):
    def __init__(self, browser) -> None:
        super().__init__(browser)

    def open(self):
        self.browser.get('https://www.qa-practice.com/elements/button/simple')

    def button(self):
        return self.find(button_selector)

    def button_is_displayed(self):
        return self.button().is_displayed()

    def result(self):
        return self.find(result_selector)
