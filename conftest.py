import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    browser = webdriver.Firefox()
    yield browser
    browser.quit()