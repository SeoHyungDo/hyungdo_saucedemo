import pytest
import time
import requests
from selenium.webdriver.common.by import By
from root_obj.standard_user_obj import standard_user_obj
from utility.passclass import passclass
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Test_standard_user(passclass) :

    # 로그인 후 URL에 inventory.html이 있는지 확인한다.
    def test_login(self):
        standard_user = standard_user_obj(self.driver)
        standard_user.input_id_standard_user_login_obj("standard_user", "secret_sauce")  # standard User Login

        wait = WebDriverWait(self.driver, 10)
        inventory_container = wait.until(
            EC.presence_of_element_located((By.ID, "inventory_container"))
        )
        assert "inventory.html" in self.driver.current_url

    def test_left_menu(self):
        standard_user = standard_user_obj(self.driver)
        standard_user.hamburger_menu_click()

        assert standard_user.side_bar_menu('All_Items') == "All Items"
        assert standard_user.side_bar_menu('About') == "About"
        assert standard_user.side_bar_menu('Logout') == "Logout"
        assert standard_user.side_bar_menu('Reset_App_State') == "Reset App State"