import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base_page import BasePage 


class MainPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
    
    @allure.step("Вернуть текст элемента")
    def return_element_text(self,locator):
        return self.wait_and_find_element(locator).text