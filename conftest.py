import pytest
from selenium import webdriver
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

@pytest.fixture(scope="function")
def driver():
    browser = webdriver.Firefox()
    yield browser
    browser.quit()
