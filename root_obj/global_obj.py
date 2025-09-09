from http.client import responses
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests


class global_menu:
    def __init__(self, driver):  # 생성자, 객체를 생성할 때 driver객체를 인자로 넣어 줄 것이라 생각하고 그 driver 객체를 받아 self.driver에 할당
        self.driver = driver

    top_logo = (By.XPATH,'//*[@id="header_container"]/div[1]/div[2]/div')
    hamburger_menu = (By.CLASS_NAME, 'bm-burger-button')
    cart_button = (By.XPATH, '//*[@id="shopping_cart_container"]/a')
    cart_button_badge = (By.XPATH, '//*[@id="shopping_cart_container"]/a/span')

    def top_logo_obj(self):
        return self.driver.find_element(*global_menu.top_logo)

    def top_logo_text(self) :
        return self.driver.find_element(*self.top_logo).text

    def hamburger_menu_obj(self) :
        return self.driver.find_element(*self.hamburger_menu)

    def side_bar_all_items(self):
        return self.driver.find_element(By.XPATH,'//*[@id="inventory_sidebar_link"]')

    def side_bar_all_items_text(self):
        return self.driver.find_element(By.XPATH,'//*[@id="inventory_sidebar_link"]').text

    def side_bar_about(self):
        return self.driver.find_element(By.XPATH, '//*[@id="about_sidebar_link"]')

    def side_bar_about_text(self):
        return self.driver.find_element(By.XPATH, '//*[@id="about_sidebar_link"]').text

    def side_bar_logout(self):
        return self.driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]')

    def side_bar_logout_text(self):
        return self.driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').text

    def side_bar_reset_app_state(self):
        return self.driver.find_element(By.XPATH, '//*[@id="reset_sidebar_link"]')

    def side_bar_reset_app_text(self):
        return self.driver.find_element(By.XPATH, '//*[@id="reset_sidebar_link"]').text

    def side_bar_x_button(self):
        return self.driver.find_element(By.XPATH, '//*[@id="react-burger-cross-btn"]')

    def cart_button_obj(self):
        return self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')

    def cart_button_badge_obj(self):
        return self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')

    def cart_button_badge_number(self):
        return self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text