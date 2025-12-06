import allure
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from main_page import MainPage
from base_page import BasePage
from Locators.order_page_locators import OrderPageLocators 

class OrderPage(BasePage):
    @allure.step('Заполняем поле Имя')
    def set_name(self, name):
        self.wait_and_find_element(OrderPageLocators.NAME_INPUT).send_keys(name)

    @allure.step('Заполняем поле Фамилия')
    def set_second_name(self, surname):
        self.wait_and_find_element(OrderPageLocators.SURNAME_INPUT).send_keys(surname)

    @allure.step('Заполняем поле Адрес')          
    def set_address(self, address):
        self.wait_and_find_element(OrderPageLocators.ADDRESS_INPUT).send_keys(address)

    @allure.step('Заполняем поле Станция метро')
    def set_metro_station(self, metro_station):
        self.wait_and_find_element(OrderPageLocators.METRO_INPUT).click()
        self.wait_and_find_element(OrderPageLocators.metro_station_locator(metro_station)).click()

    @allure.step('Заполняем поле Номер телефона')
    def set_phone_number(self, phone):
        self.wait_and_find_element(OrderPageLocators.PHONE_INPUT).send_keys(phone)

    @allure.step('Кликаем кнопку далее')
    def click_continue_button(self):
        self.wait_and_find_element(OrderPageLocators.NEXT_BTN).click()

    @allure.step('Выбираем дату доставки')
    def set_delivery_date(self, delivery_day):
        self.wait_and_find_element(OrderPageLocators.DATE_INPUT).click()
        self.wait_and_find_element(OrderPageLocators.choose_date(delivery_day)).click()

    @allure.step('Заполняем поле Срок Аренды')
    def set_rental_period(self, rental_period):
        self.wait_and_find_element(OrderPageLocators.TIME_PERIOD_INPUT).click()
        self.wait_and_find_element(OrderPageLocators.choose_period(rental_period)).click()

    @allure.step('Кликаем кнопку заказать')
    def click_order_button(self):
        self.wait_and_find_element(OrderPageLocators.ORDER_FINAL_BUTTON).click()

    @allure.step('Подтверждаем заказ')
    def click_confirm_button(self):
        self.wait_and_find_element(OrderPageLocators.ORDER_CONFIRM_BUTTON).click()

    @allure.step('Находим кнопку Статус Заказа')
    def find_status_button(self):
        return self.wait_and_find_element(OrderPageLocators.STATUS_BTN).is_displayed()

    @allure.step('Заказываем самокат')
    def order_scooter(self, name, surname, address, metro_station, phone, delivery_day, rental_period):
        self.set_name(name)
        self.set_second_name(surname)
        self.set_address(address)
        self.set_metro_station(metro_station)
        self.set_phone_number(phone)
        self.click_continue_button()
        self.set_delivery_date(delivery_day)
        self.set_rental_period(rental_period)
        self.click_order_button()
        self.click_confirm_button()