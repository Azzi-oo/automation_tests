from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from pages.like_a_button import LikedButtonPage


def test_button2_clicked(browser):
    like_a_button = LikedButtonPage(browser)
    like_a_button.open()
    like_a_button.button.open()
    like_a_button.button.click()
    assert 'Submitted' == like_a_button.result_text
