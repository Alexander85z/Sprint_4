
from selenium.webdriver.common.by import By


class LocatorOrderingPage:
    order_header = [By.CLASS_NAME, 'Button_Button__ra12g']
    order_footer = [By.CLASS_NAME, 'Home_FinishButton__1_cWm']
    button_next = [By.XPATH, "//button[contains(text(),'Далее')]"]
    select_button_order = [By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[contains(text(),'Заказать')]"]
    order_yes = [By.XPATH, "//button[contains(text(), 'Да')]"]
    order_complete = [By.XPATH, "//button[contains(text(), 'Посмотреть статус')]"]