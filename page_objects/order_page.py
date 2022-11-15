from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class OrderingPage():

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

    def __init__(self, driver):
        self.driver = driver


    def click_order_page(self, order_page_click):
        return self.driver.find_element(*order_page_click).click()

    def wait_click_order_page(self, order_page_click):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(order_page_click)).click()

    def input_order_page(self, order_page_input, text):
        return self.driver.find_element(*order_page_input).send_keys(text)

    def scroll_page(self):
        element = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Когда аренда заканчивается')]")
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)






    def writing_customer_page_check_1(self):
        self.input_order_page(self.input_name, "Дарт")
        self.input_order_page(self.input_surname, "Вэйдер")
        self.input_order_page(self.input_adress, "Звезда смерти")
        self.click_order_page(self.input_metro)
        self.wait_click_order_page(self.select_metro)
        self.input_order_page(self.input_phone, "89991231212")

    def writing_scooter_page_check_1(self):
        self.input_order_page(self.wright_date, '22.11.2022')
        self.wait_click_order_page(self.input_date)
        self.click_order_page(self.input_rent_time)
        self.click_order_page(self.select_1_day_rent_time)
        self.click_order_page(self.select_color_scooter)


    def writing_customer_page_check_2(self):
        self.input_order_page(self.input_name, "Энакин")
        self.input_order_page(self.input_surname, "Скайуокер")
        self.input_order_page(self.input_adress, "Татуин")
        self.click_order_page(self.input_metro)
        self.wait_click_order_page(self.select_metro)
        self.input_order_page(self.input_phone, "89991231213")

    def writing_scooter_page_check_2(self):
        self.input_order_page(self.wright_date, '23.11.2022')
        self.wait_click_order_page(self.input_date)
        self.click_order_page(self.input_rent_time)
        self.click_order_page(self.select_1_day_rent_time)
        self.click_order_page(self.select_color_scooter)






