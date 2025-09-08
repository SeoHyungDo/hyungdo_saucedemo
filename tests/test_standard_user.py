import pytest
import time
import requests
import os
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

        standard_user.side_bar_x_button().click()

    def test_product_image_check(self):
        standard_user = standard_user_obj(self.driver)
        img = self.driver.find_element(By.XPATH,'//*[@id="item_4_img_link"]/img')
        img_src = img.get_attribute("src")
        assert img_src not in  "/static/media/sl-404.168b1cce.jpg" # 이미지 이름에 해당 src가 없어야 함

    def test_first_product_product_info(self):
        standard_user = standard_user_obj(self.driver)
        actual_first_product = standard_user.first_product_info()

        print(actual_first_product.keys())

        first_product_title_expect = "Sauce Labs Backpack"
        first_product_description_expect = "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection."
        first_product_price_expect = "$29.99"
        add_to_cart_button = "Add to cart"

        assert actual_first_product["first_product_title"] == first_product_title_expect
        assert actual_first_product["first_product_description"] == first_product_description_expect
        assert actual_first_product["first_product_price"] == first_product_price_expect
        assert actual_first_product["add_to_cart"] == add_to_cart_button

    def test_first_product_move_cart(self):
        standard_user = standard_user_obj(self.driver)

        standard_user.add_to_cart_button().click()

        remove_button = standard_user.add_to_cart_click_button_after().text
        expect_remove_button = "Remove"
        assert remove_button == expect_remove_button

        cart_button_badge_count = standard_user.cart_button_badge_obj().text
        assert cart_button_badge_count == '1'

        standard_user.cart_button_obj().click()

        # 여기서 부터 cart 부분


