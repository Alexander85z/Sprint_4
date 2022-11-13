import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    driver = webdriver.Firefox(executable_path=r'C:\WebDriver\bin\geckodriver.exe', options=options)

    driver.get("https://qa-scooter.praktikum-services.ru/")
    driver.find_element(By.ID, 'rcc-confirm-button').click()
    yield driver
    driver.quit()