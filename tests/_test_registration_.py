from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
from random import randint
import test_login

class TestRegistration:
    def test_registration_success(self, name='Name', email='', password='123456'):
        if email == '':
            email = 'akonovalov_17_'+ str(randint(1000, 9999)) + '@ya.ru'
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/register')
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//div[@class="Auth_login__3hAey"]/form[@class="Auth_form__3qKeq mb-20"]')))
        elements = driver.find_elements(By.XPATH, '//form//input')
        elements[0].send_keys(name)
        elements[1].send_keys(email)
        elements[2].send_keys(password)
        driver.find_element(By.XPATH, '//form/button[text()="Зарегистрироваться"]').click()
        time.sleep(1)

        if driver.current_url != "https://stellarburgers.nomoreparties.site/login":
            raise Exception("После заполнения корректных регистрационных данных сайт не перешёл на страницу входа")

        driver.find_element(By.XPATH, '//form//input[@name="name"]').send_keys(email)
        driver.find_element(By.XPATH, '//form//input[@name="Пароль"]').send_keys(password)
        driver.find_element(By.XPATH, '//form/button[text()="Войти"]').click()
        time.sleep(1)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()
