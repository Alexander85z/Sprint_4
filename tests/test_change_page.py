from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.order_page import OrderingPage


class TestChangePage:
    order_header = [By.CLASS_NAME, 'Button_Button__ra12g']
    header_buttom_scooter = [By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']"]
    header_buttom_yandex = [By.XPATH, "//a[@href='//yandex.ru']"]

    def test_back_on_main_page(self, driver):
        main_page = OrderingPage(driver)
        main_page.click_order_page(self.order_header)
        main_page.click_order_page(self.header_buttom_scooter)

        main_page.find_element(By.CLASS_NAME, 'Button_Button__ra12g')
        sleep(3)
        elm = driver.find_element(By.XPATH, "//div[@class='Home_HomePage__ZXKIX']")
        elm_id = elm.get_attribute('class')
        assert elm_id == 'Home_HomePage__ZXKIX'

    def test_main_page_dzen(self, driver):
        maim_page = OrderingPage(driver)
        maim_page.click_order_page(self.header_buttom_yandex)
        sleep(3)

        driver.switch_to_window(driver.window_handles[1])
        elm = driver.find_element(By.XPATH, "//div[@class='dzen-desktop__teaser-3u']")
        elm_id = elm.get_attribute('class')
        assert elm_id == 'dzen-desktop__teaser-3u'

