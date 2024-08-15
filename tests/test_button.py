from selenium.webdriver.common.by import By

from pages.simple_button import SimpleButtonPage


def test_button1_exist(browser):
    simple_page = SimpleButtonPage(browser)
    simple_page.open()
    assert simple_page.button().is_displayed()


def test_button1_clicked(browser):
    simple_page = SimpleButtonPage(browser)
    simple_page.open()
    browser.find_element(By.ID, 'submit-id-submit').click()
    assert 'Submitted' == browser.find_element(By.ID, 'result-text').text
