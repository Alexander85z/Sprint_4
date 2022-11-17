from time import sleep

import allure
from selenium.webdriver.common.by import By
from page_objects.order_page import OrderingPage
from locators.locator_change_page import *




class TestChangePage:




    @allure.title('Работа кнопки "самокат"')
    def test_back_on_main_page(self, driver):
        main_page = OrderingPage(driver)
        main_page.click_order_page(order_header)
        main_page.click_order_page(header_buttom_scooter)
        elm = driver.find_element(*main_page_check_element)
        elm_id = elm.get_attribute('class')
        assert elm_id == 'Home_HomePage__ZXKIX'

    @allure.title('Работа кнопки "яндекс"')
    def test_main_page_dzen(self, driver):
        driver.find_element(*button_yandex_main).click()
        sleep(5)
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        elm = driver.find_element(*dzen_main_element)
        elm_id = elm.text
        assert elm_id == 'Удобный и быстрый Яндекс.Браузер'
