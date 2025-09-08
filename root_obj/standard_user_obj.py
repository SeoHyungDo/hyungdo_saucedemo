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

    hamburger_menu = (By.CLASS_NAME, 'bm-burger-button')
    Add_to_cart = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    Add_to_cart_click_after = (By.XPATH, '//*[@id="remove-sauce-labs-backpack"]')
    first_product_title = (By.XPATH, '//*[@id="item_4_title_link"]/div')
    first_product_description = (By.XPATH,'//*[@id="inventory_container"]/div/div[1]/div[2]/div[1]/div')
    first_product_price = (By.XPATH,'//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
    cart_button = (By.XPATH, '//*[@id="shopping_cart_container"]/a')
    cart_button_badge = (By.XPATH, '//*[@id="shopping_cart_container"]/a/span')

    def input_id_standard_user_login_obj(self, username, password): # ID에 standard_user 입력 상태
        # send_keys를 하기 전에 JavaScript를 실행해서 자동 완성 팝업을 방지
        self.driver.execute_script("document.getElementById('user-name').setAttribute('autocomplete', 'off');")
        self.driver.execute_script("document.getElementById('password').setAttribute('autocomplete', 'off');")

        self.driver.find_element(*self.input_id).send_keys(username)
        self.driver.find_element(*self.input_pw).send_keys(password)

        self.driver.find_element(*self.login_button).click()

    def hamburger_menu_obj(self) :
        return self.driver.find_element(*self.hamburger_menu)

    def side_bar_all_items(self):
        return self.driver.find_element(By.XPATH,'//*[@id="inventory_sidebar_link"]')

    def side_bar_about(self):
        return self.driver.find_element(By.XPATH, '//*[@id="about_sidebar_link"]')

    def side_bar_logout(self):
        return self.driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]')

    def side_bar_reset_app_state(self):
        return self.driver.find_element(By.XPATH, '//*[@id="reset_sidebar_link"]')

    def side_bar_x_button(self):
        return self.driver.find_element(By.XPATH, '//*[@id="react-burger-cross-btn"]')

    def add_to_cart_button(self):
        return self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')

    def add_to_cart_click_button_after(self):
        return self.driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-backpack"]')

    def cart_button_obj(self):
        return self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')

    def cart_button_badge_obj(self):
        return self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')

    def first_product_info(self):
        first_product = {
            "first_product_title" : self.driver.find_element(By.XPATH,'//*[@id="item_4_title_link"]/div').text,
            "first_product_description" : self.driver.find_element(By.XPATH,'//*[@id="inventory_container"]/div/div[1]/div[2]/div[1]/div').text,
            "first_product_price" : self.driver.find_element(By.XPATH,'//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div').text,
            "add_to_cart" : self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').text
        }
        return first_product


