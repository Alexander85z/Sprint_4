from selenium.webdriver.common.by import By


class MainPage():

    def __init__(self, driver):
        self.driver = driver

    def click_question(self, main_question):
        return self.driver.find_element(*main_question).click()

    def get_attribute_id(self):
        elm = self.driver.find_element(By.XPATH, "//div[@aria-expanded='true']")
        elm_id = elm.get_attribute('id')
        return elm_id


