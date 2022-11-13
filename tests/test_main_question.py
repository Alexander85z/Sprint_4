from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from page_objects.main_page import MainPage


class TestMainQuestion:
    main_question_0 = [By.ID, 'accordion__heading-0']
    main_question_1 = [By.ID, 'accordion__heading-1']
    main_question_2 = [By.ID, 'accordion__heading-2']
    main_question_3 = [By.ID, 'accordion__heading-3']
    main_question_4 = [By.ID, 'accordion__heading-4']
    main_question_5 = [By.ID, 'accordion__heading-5']
    main_question_6 = [By.ID, 'accordion__heading-6']
    main_question_7 = [By.ID, 'accordion__heading-7']

    def test_main_question_0(self, driver):

        ya_question = MainPage(driver)
        ya_question.click_question(self.main_question_0)
        assert ya_question.get_attribute_id() == 'accordion__heading-0'

    def test_main_question_1(self, driver):

        ya_question = MainPage(driver)
        ya_question.click_question(self.main_question_1)
        assert ya_question.get_attribute_id() == 'accordion__heading-1'

    def test_main_question_2(self, driver):

        ya_question = MainPage(driver)
        ya_question.click_question(self.main_question_2)
        assert ya_question.get_attribute_id() == 'accordion__heading-2'

    def test_main_question_3(self, driver):

        ya_question = MainPage(driver)
        ya_question.click_question(self.main_question_3)
        assert ya_question.get_attribute_id() == 'accordion__heading-3'

    def test_main_question_4(self, driver):

        ya_question = MainPage(driver)
        ya_question.click_question(self.main_question_4)
        assert ya_question.get_attribute_id() == 'accordion__heading-4'

    def test_main_question_5(self, driver):

        ya_question = MainPage(driver)
        ya_question.click_question(self.main_question_5)
        assert ya_question.get_attribute_id() == 'accordion__heading-5'

    def test_main_question_6(self, driver):

        ya_question = MainPage(driver)
        ya_question.click_question(self.main_question_6)
        assert ya_question.get_attribute_id() == 'accordion__heading-6'

    def test_main_question_7(self, driver):

        ya_question = MainPage(driver)
        ya_question.click_question(self.main_question_7)
        assert ya_question.get_attribute_id() == 'accordion__heading-7'