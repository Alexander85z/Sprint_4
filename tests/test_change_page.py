from time import sleep

import allure
from selenium.webdriver.common.by import By
from page_objects.order_page import OrderingPage




class TestChangePage:
    order_header = [By.CLASS_NAME, 'Button_Button__ra12g']
    header_buttom_scooter = [By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']"]
    header_buttom_yandex = [By.XPATH, "//a[@href='//yandex.ru']"]

    @allure.title('Работа кнопки "самокат"')
    def test_back_on_main_page(self, driver):
        main_page = OrderingPage(driver)
        main_page.click_order_page(self.order_header)
        main_page.click_order_page(self.header_buttom_scooter)
        elm = driver.find_element(By.XPATH, "//div[@class='Home_HomePage__ZXKIX']")
        elm_id = elm.get_attribute('class')
        assert elm_id == 'Home_HomePage__ZXKIX'

    @allure.title('Работа кнопки "яндекс"')
    def test_main_page_dzen(self, driver):
        driver.find_element(By.XPATH, "//a[@href='//yandex.ru']").click()
        sleep(5)
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        elm = driver.find_element(By.XPATH, "//div[contains(text(), 'Удобный и быстрый Яндекс.Браузер')]")
        elm_id = elm.text
        assert elm_id == 'Удобный и быстрый Яндекс.Браузер'
