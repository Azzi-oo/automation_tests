from pages.base import BasePage
from selenium.webdriver.common.by import By


button_selector = (By.LINK_TEXT, 'Click')
result_selector = (By.ID, 'result-text')


class LikedButtonPage(BasePage):
    def __init__(self, browser) -> None:
        super().__init__(browser)


    @property
    def button(self):
        return self.find(button_selector)

    def open(self):
        self.browser.get('https://www.qa-practice.com/elements/button/like_a_button')

    def result(self):
        return self.find(result_selector)


    @property
    def button_is_displayed(self):
        return self.button_is_displayed()


    @property
    def result(self):
        return self.find(result_selector)


    @property
    def result_text(self):
        return self.result.text
