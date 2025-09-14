from http.client import responses
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import requests
from selenium.webdriver.support import expected_conditions as EC

class standard_user_obj :

    def __init__(self, driver):
        self.driver = driver
        self.input_id = (By.ID, 'user-name')
        self.input_pw = (By.ID, 'password')
        self.login_button = (By.ID, 'login-button')


    Add_to_cart = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    Add_to_cart_click_after = (By.XPATH, '//*[@id="remove-sauce-labs-backpack"]')

    first_product_title = (By.XPATH, '//*[@id="item_4_title_link"]/div')
    first_product_description = (By.XPATH,'//*[@id="inventory_container"]/div/div[1]/div[2]/div[1]/div')
    first_product_price = (By.XPATH,'//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')

    second_product_title = (By.XPATH, '//*[@id="item_0_title_link"]/div')
    second_product_description = (By.XPATH,'//*[@id="inventory_container"]/div/div[2]/div[2]/div[1]/div')
    second_product_price = (By.XPATH,'//*[@id="inventory_container"]/div/div[2]/div[2]/div[2]/div')

    first_add_to_cart_button = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    second_add_to_cart_button = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
    remove_cart_button = (By.XPATH, '//*[@id="remove-sauce-labs-backpack"]')

    def input_id_standard_user_login_obj(self, username, password): # ID에 standard_user 입력 상태
        # send_keys를 하기 전에 JavaScript를 실행해서 자동 완성 팝업을 방지

        if "inventory" in self.driver.current_url:
            print("⚠️ 이미 로그인된 상태 → 로그인 페이지로 이동")
            self.driver.get("https://www.saucedemo.com/")

        # user-name 필드가 나타날 때까지 대기
        wait = WebDriverWait(self.driver, 10)
        self.driver.execute_script("document.getElementById('user-name').setAttribute('autocomplete', 'off');")
        self.driver.execute_script("document.getElementById('password').setAttribute('autocomplete', 'off');")

        self.driver.find_element(*self.input_id).send_keys(username)
        self.driver.find_element(*self.input_pw).send_keys(password)

        self.driver.find_element(*self.login_button).click()

        wait.until(EC.visibility_of_element_located((By.ID, "inventory_container")))

    def first_add_to_cart_button_obj(self):
        return self.driver.find_element(*self.first_add_to_cart_button)

    def first_add_to_cart_button_text(self):
        return self.driver.find_element(*self.first_add_to_cart_button).text

    def second_add_to_cart_button_obj(self):
        return self.driver.find_element(*self.second_add_to_cart_button)

    def second_add_to_cart_button_text(self):
        return self.driver.find_element(*self.second_add_to_cart_button).text

    def remove_cart_button_obj(self):
        return self.driver.find_element(*self.remove_cart_button)

    def remove_cart_button_text(self):
        return self.driver.find_element(*self.remove_cart_button).text


    def first_product_info(self):
        first_product = {
            "first_product_title" : self.driver.find_element(By.XPATH,'//*[@id="item_4_title_link"]/div').text,
            "first_product_description" : self.driver.find_element(By.XPATH,'//*[@id="inventory_container"]/div/div[1]/div[2]/div[1]/div').text,
            "first_product_price" : self.driver.find_element(By.XPATH,'//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div').text,
            "first_add_to_cart" : self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').text,
        }
        return first_product

    def second_product_info(self):
        second_product = {
            "second_product_title" : self.driver.find_element(By.XPATH, '//*[@id="item_0_title_link"]/div').text,
            "second_product_description" : self.driver.find_element(By.XPATH,'//*[@id="inventory_container"]/div/div[2]/div[2]/div[1]/div').text,
            "second_product_price" : self.driver.find_element(By.XPATH,'//*[@id="inventory_container"]/div/div[2]/div[2]/div[2]/div').text,
            "second_remove_button" : self.driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]').text
        }
        return second_product
