from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME_INPUT = [By.XPATH,'.//input[@placeholder = "* Имя"]']
    SURNAME_INPUT = [By.XPATH,'.//input[@placeholder = "* Фамилия"]']
    ADDRESS_INPUT = [By.XPATH,'.//input[@placeholder = "* Адрес: куда привезти заказ"]']
    METRO_INPUT = [By.XPATH,'.//input[@placeholder = "* Станция метро"]']
    PHONE_INPUT = [By.XPATH,'.//input[@placeholder = "* Телефон: на него позвонит курьер"]']
    NEXT_BTN = (By.XPATH, "//button[text()='Далее']")
    DATE_INPUT = [By.XPATH,'.//input[@placeholder = "* Когда привезти самокат"]']
    TIME_PERIOD_INPUT = [By.XPATH,'.//div[contains(text(),"* Срок аренды")]']
    COURIER_COMMENT_INPUT = [By.XPATH,'.//input[@placeholder = "Комментарий для курьера"]']
    ORDER_FINAL_BUTTON = [By.XPATH,'.//button[contains(@class,"Button_Middle") and contains(text(),"Заказать")]']
    ORDER_CONFIRM_BUTTON = [By.XPATH,'.//button[contains(text(),"Да")]']
    STATUS_BUTTON = [By.XPATH,'.//button[contains(text(),"Посмотреть статус")]']


    
    @staticmethod
    def metro_station_locator(station):
        return [By.XPATH,f'.//div[contains(text(),{station})]/parent::button']
    
    @staticmethod
    def choose_date(date):
        return [By.XPATH, f'.//div[contains(text(),{date})]']
    
    @staticmethod
    def choose_period(rental_period):
        return [By.XPATH,f'.//div[contains(@class, "Dropdown-option") and contains(text(),"{rental_period}")]']
    
    @staticmethod
    def choose_type(color):
        return [By.XPATH,f'.//input[@id = "{color}"]']