from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.order_page import OrderingPage

class TestOrdering:
    order_header = [By.CLASS_NAME, 'Button_Button__ra12g']
    order_footer = [By.CLASS_NAME, 'Button_UltraBig__UU3Lp']
    input_name = [By.XPATH, "//input[@placeholder='* Имя']"]
    input_surname = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    input_adress = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    input_metro = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    select_metro = [By.XPATH, "//div[contains(text(),'Сокольники')]"]
    input_phone = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    button_next = [By.XPATH, "//button[contains(text(),'Далее')]"]

    wright_date = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    input_date = [By.XPATH, "//div[@aria-label='Choose воскресенье, 20-е ноября 2022 г.']"]
    input_rent_time = [By.XPATH, "//div[contains(text(),'* Срок аренды')]"]
    select_1_day_rent_time = [By.XPATH, "//div[contains(text(),'сутки')]"]
    select_color_scooter = [By.XPATH, "//input[@id='black']"] # тут чекбокс
    select_button_order = [By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[contains(text(),'Заказать')]"]
    order_yes = [By.XPATH, "//button[contains(text(), 'Да')]"]
    order_complete = [By.XPATH, "//button[contains(text(), 'Посмотреть статус')]"]



    def test_ordering_scooter_header_button(self, driver):
        #Заполнение формы заказчика самоката
        order_page = OrderingPage(driver)

        order_page.input_order_page(self.input_name, "Дарт")
        order_page.input_order_page(self.input_surname, "Вэйдер")
        order_page.input_order_page(self.input_adress, "Звезда смерти")
        order_page.click_order_page(self.input_metro)
        order_page.wait_click_order_page(self.select_metro)
        order_page.input_order_page(self.input_phone, "89991231212")
        order_page.click_order_page(self.button_next)

        # Заполнение формы даты, цвета и времени аренды самоката
        order_page.input_order_page(self.wright_date, '22.11.2022')
        order_page.wait_click_order_page(self.input_date)
        order_page.click_order_page(self.input_rent_time)
        order_page.click_order_page(self.select_1_day_rent_time)
        order_page.click_order_page(self.select_color_scooter)
        order_page.click_order_page(self.select_button_order)
        order_page.click_order_page(self.order_yes)
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (self.order_complete))).text == 'Посмотреть статус'
        driver.quit()


    def test_ordering_scooter_footer_button(self, driver):
        #Заполнение формы заказчика самоката
        order_page = OrderingPage(driver)
        element = driver.find_element(By.XPATH, "//div[contains(text(), 'Когда аренда заканчивается')]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        order_page.wait_click_order_page(self.order_footer)
        order_page.input_order_page(self.input_name, "Дарт")
        order_page.input_order_page(self.input_surname, "Вэйдер")
        order_page.input_order_page(self.input_adress, "Звезда смерти")
        order_page.click_order_page(self.input_metro)
        order_page.wait_click_order_page(self.select_metro)
        order_page.input_order_page(self.input_phone, "89991231212")
        order_page.click_order_page(self.button_next)

        # Заполнение формы даты, цвета и времени аренды самоката
        order_page.input_order_page(self.wright_date, '22.11.2022')
        order_page.wait_click_order_page(self.input_date)
        order_page.click_order_page(self.input_rent_time)
        order_page.click_order_page(self.select_1_day_rent_time)
        order_page.click_order_page(self.select_color_scooter)
        order_page.click_order_page(self.select_button_order)
        order_page.click_order_page(self.order_yes)
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (self.order_complete))).text == 'Посмотреть статус'
        driver.quit()

    def test_back_main_page(self, driver):
        order_page = OrderingPage(driver)







