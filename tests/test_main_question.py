from selenium.webdriver.common.by import By
import allure
from page_objects.main_page import MainPage
from locators.locator_main_question import LocatorMainPage


class TestMainQuestion:


    @allure.title("Раскрытие вопроса №1")
    def test_main_question_0(self, driver):

        ya_question = MainPage(driver)
        ya_question.click_question(LocatorMainPage.main_question_0)
        assert ya_question.get_attribute_id() == 'accordion__heading-0'

    @allure.title("Раскрытие вопроса №2")
    def test_main_question_1(self, driver):

        ya_question = MainPage(driver)
        ya_question.click_question(LocatorMainPage.main_question_1)
        assert ya_question.get_attribute_id() == 'accordion__heading-1'

    @allure.title("Раскрытие вопроса №3")
    def test_main_question_2(self, driver):

        ya_question = MainPage(driver)
        ya_question.click_question(LocatorMainPage.main_question_2)
        assert ya_question.get_attribute_id() == 'accordion__heading-2'

    @allure.title("Раскрытие вопроса №4")
    def test_main_question_3(self, driver):

        ya_question = MainPage(driver)
        ya_question.click_question(LocatorMainPage.main_question_3)
        assert ya_question.get_attribute_id() == 'accordion__heading-3'

    @allure.title("Раскрытие вопроса №5")
    def test_main_question_4(self, driver):

        ya_question = MainPage(driver)
        ya_question.click_question(LocatorMainPage.main_question_4)
        assert ya_question.get_attribute_id() == 'accordion__heading-4'

    @allure.title("Раскрытие вопроса №6")
    def test_main_question_5(self, driver):

        ya_question = MainPage(driver)
        ya_question.click_question(LocatorMainPage.main_question_5)
        assert ya_question.get_attribute_id() == 'accordion__heading-5'

    @allure.title("Раскрытие вопроса №7")
    def test_main_question_6(self, driver):

        ya_question = MainPage(driver)
        ya_question.click_question(LocatorMainPage.main_question_6)
        assert ya_question.get_attribute_id() == 'accordion__heading-6'

    @allure.title("Раскрытие вопроса №8")
    def test_main_question_7(self, driver):

        ya_question = MainPage(driver)
        ya_question.click_question(LocatorMainPage.main_question_7)
        assert ya_question.get_attribute_id() == 'accordion__heading-7'