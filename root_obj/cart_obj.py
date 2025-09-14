from http.client import responses
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests


class cart:
    def __init__(self, driver):  # 생성자, 객체를 생성할 때 driver객체를 인자로 넣어 줄 것이라 생각하고 그 driver 객체를 받아 self.driver에 할당
        self.driver = driver

    # 버튼 액션과 명칭 검증 등 여러가지가 필요한 경우 변수로 선언 했습니다.
    cart_button = (By.XPATH, '//*[@id="shopping_cart_container"]/a')
    cart_button_badge = (By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    cart_remove_button = (By.XPATH, '//*[@id="remove-sauce-labs-backpack"]')
    cart_continue_shopping_button = (By.XPATH, '//*[@id="continue-shopping"]')
    cart_checkout_button = (By.XPATH, '//*[@id="checkout"]')

    cart_your_cart_title_locator = (By.XPATH, '//*[@id="header_container"]/div[2]/span')
    cart_list_qty_locator = (By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[1]')
    cart_list_description_locator = (By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[2]')

    cart_list_qty_number_1_locator = (By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[1]')
    cart_list_product_name_1_locator = (By.XPATH, '//*[@id="item_4_title_link"]/div')
    cart_list_product_description_1_locator = (By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[1]')
    cart_list_product_price_1_locator = (By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')

    cart_list_qty_number_2_locator = (By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[4]/div[1]')
    cart_list_product_name_2_locator = (By.XPATH, '//*[@id="item_0_title_link"]/div')
    cart_list_product_description_2_locator = (By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[4]/div[2]/div[1]')
    cart_list_product_price_2_locator = (By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[4]/div[2]/div[2]/div')

    def cart_your_cart_title(self):
        return self.driver.find_element(*self.cart_your_cart_title_locator).text

    def cart_button_badge_obj(self):
        return self.driver.find_element(*self.cart_button_badge).text

    def cart_list_qty(self):
        return self.driver.find_element(*self.cart_list_qty_locator).text

    def cart_list_description(self):
        return self.driver.find_element(*self.cart_list_description_locator).text

    def cart_list_qty_number_1_obj(self):
        return self.driver.find_element(*self.cart_list_qty_number_1_locator).text

    def cart_list_product_name_1_obj(self):
        return self.driver.find_element(*self.cart_list_product_name_1_locator).text

    def cart_list_product_description_1_obj(self):
        return self.driver.find_element(*self.cart_list_product_description_1_locator).text

    def cart_list_product_price_1_obj(self):
        return self.driver.find_element(*self.cart_list_product_price_1_locator).text

    def cart_list_qty_number_2_obj(self):
        return self.driver.find_element(*self.cart_list_qty_number_2_locator).text

    def cart_list_product_name_2_obj(self):
        return self.driver.find_element(*self.cart_list_product_name_2_locator).text

    def cart_list_product_description_2_obj(self):
        return self.driver.find_element(*self.cart_list_product_description_2_locator).text

    def cart_list_product_price_2_obj(self):
        return self.driver.find_element(*self.cart_list_product_price_2_locator).text

    def cart_remove_button_obj(self):
        return self.driver.find_element(*self.cart_remove_button)

    def cart_remove_button_count_obj(self):
        return self.driver.find_elements(*self.cart_remove_button)

    def cart_remove_button_text(self):
        return self.driver.find_element(*self.cart_remove_button).text

    def cart_continue_shopping_button_obj(self):
        return self.driver.find_element(self.cart_continue_shopping_button)

    def cart_continue_shopping_button_text(self):
        return self.driver.find_element(*self.cart_continue_shopping_button).text

    def cart_checkout_button_obj(self):
        return self.driver.find_element(self.cart_checkout_button)

    def cart_checkout_button_text(self):
        return self.driver.find_element(*self.cart_checkout_button).text