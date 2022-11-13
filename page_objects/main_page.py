from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait




class MainPage():

    def __init__(self, driver):
        self.driver = driver

    def click_question(self, main_question):
        return self.driver.find_element(*main_question).click()

    def get_attribute_id(self):
        elm = self.driver.find_element(By.XPATH, "//div[@aria-expanded='true']")
        elm_id = elm.get_attribute('id')
        return elm_id


#-----------------------------------------------------
#class TestMainQuestion:

#    def test_main_question_0(self, driver):
 #       main_question_7 = [By.ID, 'accordion__heading-7']
 #       ya_question = MainPage(driver)
  #      ya_question.click_question(main_question_7)
