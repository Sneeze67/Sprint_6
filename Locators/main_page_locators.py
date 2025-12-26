from selenium.webdriver.common.by import By

class MainPageLocators:
    yandex_logo = [By.XPATH,'.//a[contains(@class,"Header_LogoYandex")]']
    order_button_top = [By.XPATH,'.//div[contains(@class,"Header_Nav")]//button[contains(@class,"Button")]']
    order_button_bottom = [By.XPATH,'.//button[contains(@class,"Button_Middle")]']
    COOKIE_BTN = [By.XPATH,'.//button[contains(@class,"App_CookieButton")]']
    scooter_logo = (By.XPATH, "//img[@alt='Scooter']")
    dzen_header =(By.XPATH, './/header[@aria-label = "Шапка сайта"]') 
    
    @staticmethod
    def faq_locator(locator_id):
        return [By.XPATH,f'.//div[@id = "accordion__heading-{locator_id}"]']
    
    @staticmethod
    def faq_text(locator_id):
        return [By.XPATH,f'.//div[@id = "accordion__panel-{locator_id}"]//p']
