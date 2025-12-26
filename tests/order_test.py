import allure
import pytest
import sys
import os
sys.path += [os.path.dirname(os.path.dirname(__file__)) + p for p in ['', '/pages', '/locators', '/data']]
from data import OrderTestData
from main_page_locators import MainPageLocators
from order_page import OrderPage
from main_page import MainPage
from urls import Urls 


@allure.feature('Заказы')
class TestOrder:

    @allure.title('Проверка верхней кнопки заказа')
    @allure.description(
        'Находим сверху кнопку Заказа и нажимаем на нее')
    def test_top_order_button(self, driver):
        page = MainPage(driver)
        page.open_page(Urls.MAIN_PAGE)
        page.click_top_order_btn()
        assert page.get_current_url() == Urls.ORDER_PAGE, f"Верняя кнопка заказа ведёт на неправильную страницу"


    @allure.title('Проверка нижней кнопки заказа')
    @allure.description(
        'Находим снизу кнопку Заказа и нажимаем на нее')
    def test_bottom_order_button(self, driver):
        page = MainPage(driver)
        page.open_page(Urls.MAIN_PAGE)
        page.click_bottom_order_btn()
        assert page.get_current_url() == Urls.ORDER_PAGE, f"Нижняя кнопка заказа ведёт на неправильную страницу"

    
    @allure.title('Полная процедура заказа самоката, 2 варианта данных')
    @pytest.mark.parametrize(OrderTestData.param, OrderTestData.value)
    def test_order_scooter(self, driver, name, surname, address, metro_station, phone, delivery_day, rental_period,color, courier_comment):
        page = OrderPage(driver)
        page.open_page(Urls.ORDER_PAGE)
        page.order_scooter(name, surname, address, metro_station, phone, delivery_day, rental_period,color,courier_comment)
        assert page.find_status_button() == True


    @allure.title('Переходим на главную страницу через лого "Самокат"')
    def test_scooter_logo_redirect(self, driver):
        page = MainPage(driver)
        page.open_page(Urls.ORDER_PAGE)
        page.click_to_scooter()
        assert page.get_current_url() == Urls.MAIN_PAGE


    @allure.title('Переходим на яндекс дзен через главное лого')
    def test_yandex_logo_redirect(self, driver):
        page = MainPage(driver)
        page.open_page(Urls.ORDER_PAGE)
        page.click_to_yandex_logo()
        page.switch_to_window(1)
        page.wait_and_find_element(MainPageLocators.dzen_header).is_displayed()
        assert page.get_current_url() == Urls.DZEN_URL