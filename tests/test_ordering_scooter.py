import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.order_page import OrderingPage

class TestOrdering:
    order_header = [By.CLASS_NAME, 'Button_Button__ra12g']
    order_footer = [By.CLASS_NAME, 'Home_FinishButton__1_cWm']
    button_next = [By.XPATH, "//button[contains(text(),'Далее')]"]
    select_button_order = [By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[contains(text(),'Заказать')]"]
    order_yes = [By.XPATH, "//button[contains(text(), 'Да')]"]
    order_complete = [By.XPATH, "//button[contains(text(), 'Посмотреть статус')]"]

    @allure.title('Работа кнопки "Заказать" в хэдере 1')
    @allure.description("Набор данных 1")
    def test_ordering_scooter_header_button_check_1(self, driver):
        order_page = OrderingPage(driver)
        # Заполнение формы заказчика самоката
        order_page.wait_click_order_page(self.order_header)
        order_page.writing_customer_page_check_1()
        order_page.click_order_page(self.button_next)
        # Заполнение формы самоката
        order_page.writing_scooter_page_check_1()
        order_page.click_order_page(self.select_button_order)
        order_page.click_order_page(self.order_yes)
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (self.order_complete))).text == 'Посмотреть статус'
        driver.quit()

    @allure.title('Работа кнопки "Заказать" в футере 1')
    @allure.description("Набор данных 1")
    def test_ordering_scooter_footer_button_check_1(self, driver):

        order_page = OrderingPage(driver)
        #скролл страницы
        order_page.scroll_page()
        # Заполнение формы заказчика самоката
        order_page.wait_click_order_page(self.order_footer)
        order_page.writing_customer_page_check_1()
        order_page.click_order_page(self.button_next)

        # Заполнение формы даты, цвета и времени аренды самоката
        order_page.writing_scooter_page_check_1()
        order_page.click_order_page(self.select_button_order)
        order_page.click_order_page(self.order_yes)
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (self.order_complete))).text == 'Посмотреть статус'
        driver.quit()

    @allure.title('Работа кнопки "Заказать" в хэдере 2')
    @allure.description("Набор данных 2")
    def test_ordering_scooter_header_button_check_2(self, driver):
        order_page = OrderingPage(driver)
        # Заполнение формы заказчика самоката
        order_page.wait_click_order_page(self.order_header)
        order_page.writing_customer_page_check_2()
        order_page.click_order_page(self.button_next)
        # Заполнение формы самоката
        order_page.writing_scooter_page_check_2()
        order_page.click_order_page(self.select_button_order)
        order_page.click_order_page(self.order_yes)
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (self.order_complete))).text == 'Посмотреть статус'
        driver.quit()

    @allure.title('Работа кнопки "Заказать" в футере 2')
    @allure.description("Набор данных 2")
    def test_ordering_scooter_footer_button_check_2(self, driver):

        order_page = OrderingPage(driver)
        #скролл страницы
        order_page.scroll_page()
        # Заполнение формы заказчика самоката
        order_page.wait_click_order_page(self.order_footer)
        order_page.writing_customer_page_check_2()
        order_page.click_order_page(self.button_next)

        # Заполнение формы даты, цвета и времени аренды самоката
        order_page.writing_scooter_page_check_2()
        order_page.click_order_page(self.select_button_order)
        order_page.click_order_page(self.order_yes)
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (self.order_complete))).text == 'Посмотреть статус'
        driver.quit()










