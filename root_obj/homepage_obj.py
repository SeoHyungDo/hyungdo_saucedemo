from selenium.webdriver.common.by import By


class saucedemo_home :
    def __init__(self, driver): #생성자, 객체를 생성할 때 driver객체를 인자로 넣어 줄 것이라 생각하고 그 driver 객체를 받아 self.driver에 할당
        self.driver = driver

    login_logo = (By.XPATH,'//*[@id="root"]/div/div[1]')
    apply_store = (By.XPATH,'//*[@id="subscribeHeader"]/li[2]/a')
    apply_store_select_box = (By.XPATH, '//*[@id="subscribeHeader"]/li[2]/a')
    apply_store_select_box_data = (By.XPATH, '//*[@id="subscribeHeader"]/li[2]/p')
    login_button = (By.XPATH, '//*[@id="wa-top-bar"]/div/menu[1]/li[4]/a')
    join_button = (By.XPATH, '//*[@id="wa-top-bar"]/div/menu[1]/li[3]/a')

    def login_logo_obj(self):
        return self.driver.find_element(*saucedemo_home.login_logo)

    def apply_store_obj(self):
        return self.driver.find_element(*saucedemo_home.apply_store)

    def apply_store_select_box_obj(self):
        return self.driver.find_element(*saucedemo_home.apply_store_select_box)

    def apply_store_select_box_data_obj(self):
        return self.driver.find_elements(*saucedemo_home.apply_store_select_box_data)

    def login_button_obj(self):
        return self.driver.find_element(*saucedemo_home.login_button)

    def join_button_obj(self):
        return self.driver.find_element(*saucedemo_home.join_button)
