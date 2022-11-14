from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.order_page import OrderingPage


class TestOrdering:
    order_header = [By.CLASS_NAME, 'Button_Button__ra12g']



    def test_writing(self, driver):
        order_page = OrderingPage(driver)
        # Заполнение формы заказчика самоката
        order_page.wait_click_order_page(self.order_header)
        order_page.writing_customer_page()
        sleep(4)

    def test_ordering_scooter_footer_button(self, driver):

        order_page = OrderingPage(driver)
        #скролл страницы
        element = driver.find_element(By.XPATH, "//div[contains(text(), 'Когда аренда заканчивается')]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        # Заполнение формы заказчика самоката
        order_page.wait_click_order_page(self.order_footer)
        order_page.writing_customer_page()
        order_page.click_order_page(self.button_next)

        # Заполнение формы даты, цвета и времени аренды самоката
        order_page.writing_scooter_page()
        order_page.click_order_page(self.select_button_order)
        order_page.click_order_page(self.order_yes)
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (self.order_complete))).text == 'Посмотреть статус'
        driver.quit()