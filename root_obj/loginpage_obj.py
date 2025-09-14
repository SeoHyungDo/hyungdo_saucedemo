from http.client import responses
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class saucedemo_home:
    def __init__(self, driver): #생성자, 객체를 생성할 때 driver객체를 인자로 넣어 줄 것이라 생각하고 그 driver 객체를 받아 self.driver에 할당
        self.driver = driver
        self.input_id = (By.ID, 'user-name')
        self.input_pw = (By.ID, 'password')
        self.login_button = (By.ID, 'login-button')

    validation_text_area = (By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]/h3')
    login_top_logo = (By.XPATH,'//*[@id="root"]/div/div[1]')

    def id_pw_clear(self):
        id_input_element = self.driver.find_element(*self.input_id)
        id_input_element.send_keys(Keys.CONTROL + "a")
        id_input_element.send_keys(Keys.BACKSPACE)

        pw_input_element = self.driver.find_element(*self.input_pw)
        pw_input_element.send_keys(Keys.CONTROL + "a")
        pw_input_element.send_keys(Keys.BACKSPACE)

    def login_top_logo_text(self):
        return self.driver.find_element(*self.login_top_logo).text

    def input_id_obj(self): # login > ID 경로
        return self.driver.find_element(*self.input_id)

    def validation_text_area_obj(self):
        return self.driver.find_element(*self.validation_text_area)

    def validation_text_area_text(self):
        return self.driver.find_element(*self.validation_text_area).text

    def input_id_standard_user_login_obj(self, username, password):
        self.driver.execute_script("document.getElementById('user-name').setAttribute('autocomplete', 'off');")
        self.driver.execute_script("document.getElementById('password').setAttribute('autocomplete', 'off');")

        self.driver.find_element(*self.input_id).send_keys(username)
        self.driver.find_element(*self.input_pw).send_keys(password)

        self.driver.find_element(*self.login_button).click()

    def input_pw_obj(self): # login > PW 경로
        return self.driver.find_element(*self.input_pw)

    def input_pw_exist_obj(self): # pw에 공통 비밀번호 입력 상태
        return self.driver.find_element(*self.input_pw).send_keys("secret_sauce")

    def login_button_obj(self): # 로그인 버튼 위치
        return self.driver.find_element(*self.login_button)
    
    def login_button_click_obj(self): # pw에 공통 비밀번호 입력 상태
        return self.driver.find_element(*self.login_button).click()