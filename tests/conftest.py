import pytest
from selene.support.shared import browser
from selenium import webdriver


@pytest.fixture(scope='session', autouse=True)
def config_browser():
    driver = webdriver.Chrome()
    browser.config.driver = driver
    browser.open('https://google.com')
    driver.set_window_size(1920, 1080)
    yield
    browser.quit()
