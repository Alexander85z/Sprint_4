import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.order_page import OrderingPage
from locators.locator_ordering_scooter import LocatorOrderingPage

class TestOrdering:


    @allure.title('Работа кнопки "Заказать" в хэдере 1')
    @allure.description("Набор данных 1")
    def test_ordering_scooter_header_button_check_1(self, driver):
        order_page = OrderingPage(driver)
        # Заполнение формы заказчика самоката
        order_page.wait_click_order_page(LocatorOrderingPage.order_header)
        order_page.writing_customer_page_check_1()
        order_page.click_order_page(LocatorOrderingPage.button_next)
        # Заполнение формы самоката
        order_page.writing_scooter_page_check_1()
        order_page.click_order_page(LocatorOrderingPage.select_button_order)
        order_page.click_order_page(LocatorOrderingPage.order_yes)
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (order_complete))).text == 'Посмотреть статус'
        driver.quit()

    @allure.title('Работа кнопки "Заказать" в футере 1')
    @allure.description("Набор данных 1")
    def test_ordering_scooter_footer_button_check_1(self, driver):

        order_page = OrderingPage(driver)
        #скролл страницы
        order_page.scroll_page()
        # Заполнение формы заказчика самоката
        order_page.wait_click_order_page(LocatorOrderingPage.order_footer)
        order_page.writing_customer_page_check_1()
        order_page.click_order_page(LocatorOrderingPage.button_next)

        # Заполнение формы даты, цвета и времени аренды самоката
        order_page.writing_scooter_page_check_1()
        order_page.click_order_page(LocatorOrderingPage.select_button_order)
        order_page.click_order_page(LocatorOrderingPage.order_yes)
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (LocatorOrderingPage.order_complete))).text == 'Посмотреть статус'
        driver.quit()

    @allure.title('Работа кнопки "Заказать" в хэдере 2')
    @allure.description("Набор данных 2")
    def test_ordering_scooter_header_button_check_2(self, driver):
        order_page = OrderingPage(driver)
        # Заполнение формы заказчика самоката
        order_page.wait_click_order_page(LocatorOrderingPage.order_header)
        order_page.writing_customer_page_check_2()
        order_page.click_order_page(LocatorOrderingPage.button_next)
        # Заполнение формы самоката
        order_page.writing_scooter_page_check_2()
        order_page.click_order_page(LocatorOrderingPage.select_button_order)
        order_page.click_order_page(LocatorOrderingPage.order_yes)
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (LocatorOrderingPage.order_complete))).text == 'Посмотреть статус'
        driver.quit()

    @allure.title('Работа кнопки "Заказать" в футере 2')
    @allure.description("Набор данных 2")
    def test_ordering_scooter_footer_button_check_2(self, driver):

        order_page = OrderingPage(driver)
        #скролл страницы
        order_page.scroll_page()
        # Заполнение формы заказчика самоката
        order_page.wait_click_order_page(LocatorOrderingPage.order_footer)
        order_page.writing_customer_page_check_2()
        order_page.click_order_page(LocatorOrderingPage.button_next)

        # Заполнение формы даты, цвета и времени аренды самоката
        order_page.writing_scooter_page_check_2()
        order_page.click_order_page(LocatorOrderingPage.select_button_order)
        order_page.click_order_page(LocatorOrderingPage.order_yes)
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (LocatorOrderingPage.order_complete))).text == 'Посмотреть статус'
        driver.quit()










