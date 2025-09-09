import pytest
import time
import requests
import os

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from root_obj.standard_user_obj import standard_user_obj
from utility.passclass import passclass
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from root_obj.standard_user_obj import standard_user_obj
from root_obj.global_obj import global_menu
from root_obj.cart_obj import cart

class Test_standard_user(passclass) :

    # 로그인 후 URL에 inventory.html이 있는지 확인한다.

    def test_login(self):
        standard_user = standard_user_obj(self.driver)
        standard_user.input_id_standard_user_login_obj("standard_user", "secret_sauce")  # standard User Login

        wait = WebDriverWait(self.driver, 10)
        inventory_container = wait.until(
            EC.presence_of_element_located((By.ID, "inventory_container"))
        )
        assert "inventory.html" in self.driver.current_url # Url에 inventory.html이 포함 확인

    def test_left_menu(self):
        global_obj = global_menu(self.driver)

        global_obj.hamburger_menu_obj().click()

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, "inventory_sidebar_link"))) # 명시적대기, 읽을수 있는 상태까지 대기
        
        expected_text_All_Items = "All Items"
        assert global_obj.side_bar_all_items_text() == expected_text_All_Items # 햄버거 메뉴 - All Items 노출 확인

        expected_text_About = "About"
        assert global_obj.side_bar_about_text() == expected_text_About

        expected_text_Logout = "Logout"
        assert global_obj.side_bar_logout_text() == expected_text_Logout

        expected_text_Reset_App_State = "Reset App State"
        assert global_obj.side_bar_reset_app_text() == expected_text_Reset_App_State

        global_obj.side_bar_x_button().click()

    def test_product_image_check(self):
        standard_user = standard_user_obj(self.driver)
        img = self.driver.find_element(By.XPATH,'//*[@id="item_4_img_link"]/img')
        img_src = img.get_attribute("src")
        assert img_src not in  "/static/media/sl-404.168b1cce.jpg" # 이미지 이름에 해당 src가 없어야 하는 부분 확인

    def test_first_product_product_info(self):
        standard_user = standard_user_obj(self.driver)

        actual_first_product = standard_user.first_product_info()

        print(actual_first_product.keys())

        first_product_title_expect = "Sauce Labs Backpack"
        first_product_description_expect = "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection."
        first_product_price_expect = "$29.99"
        add_to_cart_button = "Add to cart"

        assert actual_first_product["first_product_title"] == first_product_title_expect # 첫번째 상품 상품명 확인
        assert actual_first_product["first_product_description"] == first_product_description_expect # 첫번째 상품 Description 확인
        assert actual_first_product["first_product_price"] == first_product_price_expect # 첫번째 상품 가격 확인
        assert actual_first_product["add_to_cart"] == add_to_cart_button # 첫번째 상품 add to cart 버튼 확인

    def test_first_product_move_cart(self):
        standard_user = standard_user_obj(self.driver)
        global_obj = global_menu(self.driver)

        standard_user.add_to_cart_button().click()

        expect_remove_button = "Remove"
        assert standard_user.remove_cart_button_text() == expect_remove_button # remove 버튼 노출 확인
        assert global_obj.cart_button_badge_number() == '1' # 상단 cart 아이콘 카운트 1 노출 확인

        global_obj.cart_button_obj().click()

        # 여기서 부터 cart 부분

    def test_cart_left_menu(self):
        standard_user = standard_user_obj(self.driver)
        global_obj = global_menu(self.driver)

        global_obj.hamburger_menu_obj().click()

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, "inventory_sidebar_link")))  # 명시적대기, 읽을수 있는 상태까지 대기

        expected_text_All_Items = "All Items"
        assert global_obj.side_bar_all_items_text() == expected_text_All_Items

        expected_text_About = "About"
        assert global_obj.side_bar_about_text() == expected_text_About

        expected_text_Logout = "Logout"
        assert global_obj.side_bar_logout_text() == expected_text_Logout

        expected_text_Reset_App_State = "Reset App State"
        assert global_obj.side_bar_reset_app_text() == expected_text_Reset_App_State

        global_obj.side_bar_x_button().click()

    def test_cart_base_ui(self):
        global_obj = global_menu(self.driver)
        cart_obj = cart(self.driver)

        assert global_obj.top_logo_text() == "Swag Labs" # Cart > 로고 명칭 확인
        assert global_obj.cart_button_badge_number() == '1'  # Cart > 상단 cart 아이콘 카운트 1 노출 확인
        assert cart_obj.cart_your_cart_title() == "Your Cart" # Cart > Your Cart Title 확인
        assert cart_obj.cart_list_qty() == "QTY" # Cart > List > QTY 명칭 확인
        assert cart_obj.cart_list_description() == "Description" # Cart > List > Description 명칭 확인
        assert cart_obj.cart_list_qty_number_1_obj() == "1"  # Cart > List > Qty > 1 노츨 확인
        assert cart_obj.cart_list_product_name_1_obj() == "Sauce Labs Backpack"  # Cart > List > Cart에 추가된 상품명 확인
        assert cart_obj.cart_list_product_description_1_obj() == "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection."  # Cart > List > Cart에 추가된 상품 Description 확인
        assert cart_obj.cart_list_product_price_1_obj() == "$29.99" # Cart > List > Cart에 추가된 상품 가격 확인
        assert cart_obj.cart_remove_button_text() == "Remove" # Cart > Remove 버튼 확인
        assert cart_obj.cart_continue_shopping_button_text() == "Continue Shopping" # Cart > Continue 버튼 확인
        assert cart_obj.cart_checkout_button_text() == "Checkout" # Cart > Continue 버튼 확인

    def test_cart_remove_action(self):
        global_obj = global_menu(self.driver)
        cart_obj = cart(self.driver)

        cart_obj.cart_remove_button_obj().click()

        # assert global_obj.top_logo_text() == "Swag Labs"  # Cart > 로고 명칭 확인
        # assert not cart_obj.cart_button_badge
        # assert cart_obj.cart_your_cart_title() == "Your Cart"  # Cart > Your Cart Title 확인
        # assert cart_obj.cart_list_qty() == "QTY"  # Cart > List > QTY 명칭 확인
        # assert cart_obj.cart_list_description() == "Description"  # Cart > List > Description 명칭 확인
        # assert len(self.driver.find_elements(*cart_obj.cart_list_qty_number_1_obj)) == 0  # Cart > List > Qty > 1 제거 확인
        # assert len(self.driver.find_elements(*cart_obj.cart_list_product_name_1_obj)) == 0  # Cart > List > Cart에 추가된 상품명 제거 확인
        # assert len(self.driver.find_elements(*cart_obj.cart_list_product_description_1_obj)) == 0 # Cart > List > Cart에 추가된 상품 Description 제거 확인
        # assert len(self.driver.find_elements(*cart_obj.cart_list_product_price_1_obj)) == 0  # Cart > List > Cart에 추가된 상품 가격 제거 확인
        # assert len(self.driver.find_elements(*cart_obj.cart_remove_button_obj)) == 0  # Cart > Remove 버튼 제거 확인
        # assert cart_obj.cart_continue_shopping_button_text() == "Continue Shopping"  # Cart > Continue 버튼 확인
        # assert cart_obj.cart_checkout_button_text() == "Checkout"  # Cart > Continue 버튼 확인
