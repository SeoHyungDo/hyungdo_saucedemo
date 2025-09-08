from http.client import responses
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests

class standard_user_obj :

    def __init__(self, driver):
        self.driver = driver
        self.input_id = (By.ID, 'user-name')
        self.input_pw = (By.ID, 'password')
        self.login_button = (By.ID, 'login-button')

    hamburger_menu = (By.CLASS_NAME, 'bm-burger-menu')

    def input_id_standard_user_login_obj(self, username, password): # ID에 standard_user 입력 상태
        # send_keys를 하기 전에 JavaScript를 실행해서 자동 완성 팝업을 방지
        self.driver.execute_script("document.getElementById('user-name').setAttribute('autocomplete', 'off');")
        self.driver.execute_script("document.getElementById('password').setAttribute('autocomplete', 'off');")

        self.driver.find_element(*self.input_id).send_keys(username)
        self.driver.find_element(*self.input_pw).send_keys(password)

        self.driver.find_element(*self.login_button).click()

    def hamburger_menu_click(self) :
        return self.driver.find_element(*standard_user_obj.hamburger_menu).click()

    def side_bar_menu(self):
        All_Items = self.driver.find_element(By.ID,'inventory_sidebar_link')
        About = self.driver.find_element(By.ID, 'about_sidebar_link')
        Logout = self.driver.find_element(By.ID, 'logout_sidebar_link')
        Reset_App_State = self.driver.find_element(By.ID, 'reset_sidebar_link')