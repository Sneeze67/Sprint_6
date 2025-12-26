import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import sys
import os
sys.path += [os.path.dirname(os.path.dirname(__file__)) + p for p in ['', '/pages', '/locators', '/data']]
from main_page import MainPage
from main_page_locators import MainPageLocators
from data import FAQidAndAnswers
from urls import Urls


@allure.feature("FAQ")
class TestFaq:
    @pytest.mark.parametrize("locator_id",range(8))
    @allure.title('Проверка ответа на вопрос {locator_id + 1}')
    def test_faq_answers_correct_answers(self,driver,locator_id):
        main_page = MainPage(driver)
        main_page.close_cookie_banner()
        main_page.open_page(Urls.MAIN_PAGE)
        main_page.scroll_to_element(MainPageLocators.faq_locator(locator_id))
        main_page.wait_and_find_element(MainPageLocators.faq_locator(locator_id)).click()
        assert main_page.return_element_text(MainPageLocators.faq_text(locator_id)) == FAQidAndAnswers.values[locator_id]