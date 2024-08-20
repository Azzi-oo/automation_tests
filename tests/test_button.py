from selenium.webdriver.common.by import By
import allure
from pages.simple_button import SimpleButtonPage


@allure.feature('Simple button')
@allure.story('existance')
def test_button1_exist(browser):
    with allure.step('Open the page'):
        simple_page = SimpleButtonPage(browser)
        simple_page.open()
    with allure.step('Check the buttton'):
        assert simple_page.is_displayed()


@allure.feature('Simple button')
@allure.story('clickable')
def test_button1_clicked(browser):
    with allure.step('Open the page'):
        simple_page = SimpleButtonPage(browser)
        simple_page.open()
    with allure.step('Click the button'):
        simple_page.click_button()
    with allure.step('Check the result'):
        assert 'Submitted' == simple_page.result_text
