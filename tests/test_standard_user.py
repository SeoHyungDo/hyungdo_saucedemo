import pytest
import time
import requests
from selenium.webdriver.common.by import By
from root_obj.standard_user_obj import standard_user_obj
from utility.passclass import passclass
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from root_obj.standard_user_obj import standard_user_obj

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

        standard_user.hamburger_menu_obj().click()

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, "inventory_sidebar_link"))) # 명시적대기, 읽을수 있는 상태까지 대기
        
        expected_text_All_Items = "All Items"
        All_Items_text = standard_user.side_bar_all_items().text
        assert All_Items_text == expected_text_All_Items

        expected_text_About = "About"
        About_text = standard_user.side_bar_about().text
        assert About_text == expected_text_About

        expected_text_Logout = "Logout"
        Logout_text = standard_user.side_bar_logout().text
        assert Logout_text == expected_text_Logout

        expected_text_Reset_App_State = "Reset App State"
        Reset_App_State_text = standard_user.side_bar_reset_app_state().text
        assert Reset_App_State_text == expected_text_Reset_App_State