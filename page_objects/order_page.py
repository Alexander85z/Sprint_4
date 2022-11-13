from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class OrderingPage():


    def __init__(self, driver):
        self.driver = driver
        self.input_name = [By.XPATH, "//input[@placeholder='* Имя']"]
        self.input_surname = [By.XPATH, "//input[@placeholder='* Фамилия']"]
        self.input_adress = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
        self.input_metro = [By.XPATH, "//input[@placeholder='* Станция метро']"]
        self.select_metro = [By.XPATH, "//div[contains(text(),'Сокольники')]"]
        self.input_phone = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
        self.button_next = [By.XPATH, "//button[contains(text(),'Далее')]"]

    def click_order_page(self, order_page_click):
        return self.driver.find_element(*order_page_click).click()

    def wait_click_order_page(self, order_page_click):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(order_page_click)).click()

    def input_order_page(self, order_page_input, text):
        return self.driver.find_element(*order_page_input).send_keys(text)



    def writing_customer_page(self):
        self.driver.input_order_page(self.input_name, "Дарт")
        self.driver.input_order_page(self.input_surname, "Вэйдер")
        self.driver.input_order_page(self.input_adress, "Звезда смерти")
        self.driver.click_order_page(self.input_metro)
        self.driver.wait_click_order_page(self.select_metro)
        self.driver.input_order_page(self.input_phone, "89991231212")
        self.driver.click_order_page(self.button_next)




