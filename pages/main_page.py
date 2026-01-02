import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from Locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
    
    @allure.step("Вернуть текст элемента")
    def return_element_text(self,locator):
        return self.wait_and_find_element(locator).text
    
    @allure.step("Клик по верхней кнопке заказа")
    def click_top_order_btn(self):
        self.wait_and_find_element(MainPageLocators.order_button_top).click()

    @allure.step("Клик по нижней кнопке заказа")
    def click_bottom_order_btn(self):
        self.scroll_to_element(MainPageLocators.order_button_bottom)
        self.wait_and_find_element(MainPageLocators.order_button_bottom).click()

    @allure.step("Клик по логотипу Яндекса")
    def click_to_yandex_logo(self):
        self.wait_and_find_element(MainPageLocators.yandex_logo).click()

    @allure.step("Клик по лого самоката")
    def click_to_scooter(self):
        self.wait_and_find_element(MainPageLocators.scooter_logo).click()