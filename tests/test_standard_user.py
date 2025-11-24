import pytest
import time
import requests
import os

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from root_obj.standard_user_obj import standard_user_obj
from utility.passclass import PassClass
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from root_obj.standard_user_obj import standard_user_obj
from root_obj.global_obj import global_menu
from root_obj.cart_obj import cart

class Test_standard_user(PassClass) :

    # 로그인 후 URL에 inventory.html이 있는지 확인한다.

    def test_login(self):
        standard_user = standard_user_obj(self.driver)
        standard_user.input_id_standard_user_login_obj("standard_user", "secret_sauce")  # standard User Login

        wait = WebDriverWait(self.driver, 10)
        inventory_container = wait.until(
            EC.presence_of_element_located((By.ID, "inventory_container"))
        )
        assert "inventory.html" in self.driver.current_url # Url에 inventory.html이 포함 확인

    # products title 노출여부를 확인한다.
    def test_product_title(self):
        standard_user = standard_user_obj(self.driver)

        product_title_expect = "Products"

        assert standard_user.product_title_text() == product_title_expect


    # sort SelectBox에 노출되는 Text가 기대값과 일치하는지 확인한다.
    def test_sort_select_box(self):
        standard_user = standard_user_obj(self.driver)

        sort_select_box_expect = standard_user.sort_select_box_text()
        standard_user.sort_select_box_click_obj().click()

        sort_select_box_elements = self.driver.find_elements(
            By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option'
        )
        sort_select_box_actual = [el.text for el in sort_select_box_elements]

        assert sort_select_box_actual == sort_select_box_expect, \
            f"Expected {sort_select_box_expect}, but got {sort_select_box_actual}"

    # 좌측 햄버거 메뉴 명칭이 기대값과 일치하는지 확인한다.
    def test_left_menu(self):
        global_obj = global_menu(self.driver)

        global_obj.hamburger_menu_obj().click()

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, "inventory_sidebar_link"))) # 명시적대기, 읽을수 있는 상태까지 대기

    def test_left_menu_All_Items_button_name(self):
        expected_text_All_Items = "All Items"
        assert self.global_obj.side_bar_all_items_text() == expected_text_All_Items # 햄버거 메뉴 - All Items 노출 확인

    def test_left_menu_About_button_name(self):
        expected_text_About = "About"
        assert self.global_obj.side_bar_about_text() == expected_text_About

    def test_left_menu_logout_button_name(self):
        expected_text_Logout = "Logout"
        assert self.global_obj.side_bar_logout_text() == expected_text_Logout

    def test_left_menu_Reset_app_state_button_name(self):
        expected_text_Reset_App_State = "Reset App State"
        assert self.global_obj.side_bar_reset_app_text() == expected_text_Reset_App_State
        self.global_obj.side_bar_x_button_obj().click()



    # # 픽스쳐 클래스로 일괄 사용시 프레임 터지는 현상 발생하여 다른 코드에 영향을 주는 현상이 있어, 해당 이슈가 다른 테스트에 영향을 주지 않도록 해당 기능 3개 TC는 함수 단위로 픽스쳐 샤용
    # @pytest.mark.usefixtures("setup_function")
    # def test_twitter_button_action(self):
    #     global_obj = global_menu(self.driver)
    #
    #     standard_user = standard_user_obj(self.driver)
    #     standard_user.input_id_standard_user_login_obj("standard_user", "secret_sauce")  # standard User Login
    #
    #
    #
    #     WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located((By.ID, "inventory_container"))
    #     )
    #
    #     global_obj.twitter_button_tab_action()
    #     twitter_url = global_obj.twitter_button_tab_action()
    #     assert "https://x.com/saucelabs" in twitter_url  # Url에 https://x.com/saucelabs 포함 확인

    # @pytest.mark.usefixtures("setup_function")
    # def test_facebook_button_action(self):
    #     global_obj = global_menu(self.driver)
    #
    #     standard_user = standard_user_obj(self.driver)
    #     standard_user.input_id_standard_user_login_obj("standard_user", "secret_sauce")  # standard User Login
    #
    #     WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located((By.ID, "inventory_container"))
    #     )
    #
    #     global_obj.facebook_button_tab_action()
    #     self.driver.execute_script("arguments[0].scrollIntoView(true);", global_obj.twitter_button_obj())
    #     facebook_url = global_obj.facebook_button_tab_action()
    #     assert "https://www.facebook.com/saucelabs" in facebook_url  # Url에 https://www.facebook.com/saucelabs 포함 확인
    #
    #
    # @pytest.mark.usefixtures("setup_function")
    # def test_linkedin_button_action(self):
    #     global_obj = global_menu(self.driver)
    #
    #     standard_user = standard_user_obj(self.driver)
    #     standard_user.input_id_standard_user_login_obj("standard_user", "secret_sauce")  # standard User Login
    #
    #     WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located((By.ID, "inventory_container"))
    #     )
    #
    #     global_obj.linkedin_button_tab_action()
    #     self.driver.execute_script("arguments[0].scrollIntoView(true);", global_obj.twitter_button_obj())
    #     linkedin_url = global_obj.linkedin_button_tab_action()
    #     assert "https://www.linkedin.com/authwall" in linkedin_url  # Url이 너무 길어서 일부만 포함하는 내용으로 확인함 (로그인 페이지임)

    # Footer text가 기대값에 맞게 노출되는지 확인한다.
    def test_footer_text_check(self):
        footer_text_expect = '© 2025 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy'
        assert self.global_obj.footer_text_obj() == footer_text_expect

    def test_product_image_check(self):
        img = self.driver.find_element(By.XPATH,'//*[@id="item_4_img_link"]/img')
        img_src = img.get_attribute("src")
        assert img_src not in  "/static/media/sl-404.168b1cce.jpg" # 이미지 이름에 해당 src가 없어야 하는 부분 확인

    def test_first_product_product_info(self):
        actual_first_product = self.standard_user.first_product_info()

    def test_first_product_title_name(self):
        self.standard_user.first_product_info()
        self.standard_user.first_product_expect_text()

        assert (
                self.standard_user.actual_first_product["first_product_title"]
                == self.standard_user.first_product_title_expect
        )

    def test_first_product_description(self):
        self.standard_user.first_product_info()
        self.standard_user.first_product_expect_text()

        assert (
                self.standard_user.actual_first_product["first_product_description"]
                == self.standard_user.first_product_description_expect
        )

    def test_first_product_price(self):
        self.standard_user.first_product_info()
        self.standard_user.first_product_expect_text()

        assert (
                self.standard_user.actual_first_product["first_product_price"]
                == self.standard_user.first_product_price_expect
        )

    def test_first_add_to_cart(self):
        self.standard_user.first_product_info()
        self.standard_user.first_product_expect_text()

        assert (
                self.standard_user.actual_first_product["first_add_to_cart"]
                == self.standard_user.first_add_to_cart_button_text
        )

    def test_first_product_move_cart(self):
        self.standard_user.first_add_to_cart_button_obj().click()

    def test_remove_button_exist(self):
        expect_remove_button = "Remove"
        assert self.standard_user.remove_cart_button_text() == expect_remove_button # remove 버튼 노출 확인

    def test_cart_count_1(self):
        assert self.global_obj.cart_button_badge_number_obj() == '1' # 상단 cart 아이콘 카운트 1 노출 확인

        self.global_obj.cart_button_obj().click()

        # 여기서 부터 cart 부분

    def test_cart_left_menu_All_Items_text(self):
        self.global_obj.hamburger_menu_obj().click()

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, "inventory_sidebar_link")))  # 명시적대기, 읽을수 있는 상태까지 대기

        expected_text_All_Items = "All Items"
        assert self.global_obj.side_bar_all_items_text() == expected_text_All_Items

    def test_cart_left_menu_About_text(self):
        expected_text_About = "About"
        assert self.global_obj.side_bar_about_text() == expected_text_About

    def test_cart_left_menu_Logout_text(self):
        expected_text_Logout = "Logout"
        assert self.global_obj.side_bar_logout_text() == expected_text_Logout

    def test_cart_left_menu_Reset_App_state_text(self):
        expected_text_Reset_App_State = "Reset App State"
        assert self.global_obj.side_bar_reset_app_text() == expected_text_Reset_App_State

        self.global_obj.side_bar_x_button_obj().click()

    def test_first_cart_page_logo_text(self):
        assert self.global_obj.top_logo_text() == "Swag Labs" # Cart > 로고 명칭 확인

    def test_first_cart_page_badge_number_1(self):
        assert self.global_obj.cart_button_badge_number_obj() == '1'  # Cart > 상단 cart 아이콘 카운트 1 노출 확인
        
    def test_first_cart_page_your_cart_text(self):
        assert self.cart.cart_your_cart_title() == "Your Cart" # Cart > Your Cart Title 확인

    def test_first_cart_list_QTY_text(self):
        assert self.cart.cart_list_qty() == "QTY" # Cart > List > QTY 명칭 확인

    def test_first_cart_page_description_text(self):
        assert self.cart.cart_list_description() == "Description" # Cart > List > Description 명칭 확인

    def test_first_cart_list_QTY_number_1(self):
        assert self.cart.cart_list_qty_number_1_obj() == "1"  # Cart > List > Qty > 1 노츨 확인

    def test_first_cart_list_product_name_1(self):
        assert self.cart.cart_list_product_name_1_obj() == "Sauce Labs Backpack"  # Cart > List > Cart에 추가된 상품명 확인

    def test_first_cart_list_product_description_1(self):
        assert self.cart.cart_list_product_description_1_obj() == "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection."  # Cart > List > Cart에 추가된 상품 Description 확인

    def test_first_cart_list_product_price_1(self):
        assert self.cart.cart_list_product_price_1_obj() == "$29.99" # Cart > List > Cart에 추가된 상품 가격 확인

    def test_first_cart_list_Remove_button_text(self):
        assert self.cart.cart_remove_button_text() == "Remove" # Cart > Remove 버튼 확인

    def test_first_cart_list_continue_shopping_button_text(self):
        assert self.cart.cart_continue_shopping_button_text() == "Continue Shopping" # Cart > Continue 버튼 확인

    def test_first_cart_list_checkout_button_text(self):
        assert self.cart.cart_checkout_button_text() == "Checkout" # Cart > Continue 버튼 확인

    def test_cart_remove_action_logo(self):
        self.cart.cart_remove_button_obj().click()
        assert self.global_obj.top_logo_text() == "Swag Labs" # cart 상단 페이지 로고 노출

    def test_cart_remove_action_your_cart_title(self):
        assert self.cart.cart_your_cart_title() == "Your Cart" # 카트 메뉴 명칭 노출

    def test_cart_remove_action_QTY_title(self):
        assert self.cart.cart_list_qty() == "QTY" # QTY 테이블 명칭 노출

    def test_cart_remove_action_Description_title(self):
        assert self.cart.cart_list_description() == "Description" # Description 명칭 노출

    def test_cart_remove_action_continue_shopping_button_text(self):
        assert self.cart.cart_continue_shopping_button_text() == "Continue Shopping" # Continue Shopping 버튼 명 노출

    def test_cart_remove_action_Checkout_button_text(self):
        assert self.cart.cart_checkout_button_text() == "Checkout" # Checkout 버튼 명 노출

    def test_cart_remove_action_button_badge_not_exist(self):
        assert not self.driver.find_elements(*self.cart.cart_button_badge) # Cart 아이콘 뱃지가 노출되지 않아야 PASS

    def test_cart_remove_action_QTY_1_not_exist(self):
        assert not self.driver.find_elements(*self.cart.cart_list_qty_number_1_locator) # Cart List 내 QTY 1이 노출되지 않아야 정상

    def test_cart_remove_action_product_name_1_not_exist(self):
        assert not self.driver.find_elements(*self.cart.cart_list_product_name_1_locator) # Cart List 내 상품 명이 노출되지 않아야 정상

    def test_cart_remove_action_product_description_1_not_exist(self):
        assert not self.driver.find_elements(*self.cart.cart_list_product_description_1_locator) # Cart List 내 상품 설명이 노출되지 않아야 정상

    def test_cart_remove_action_product_price_1_not_exist(self):
        assert not self.driver.find_elements(*self.cart.cart_list_product_price_1_locator) # Cart List 내 상품 가격이 노출되지 않아야 정상

    def test_cart_remove_action_remove_button_not_exist(self):
        assert not self.driver.find_elements(*self.cart.cart_remove_button_count_obj()) # 이미 삭제되었으므로, remove 버튼이 노출되지 않아야 정상

    # 햄버거 메뉴를 안누르는 문제
        self.global_obj.hamburger_menu_obj().click()
        self.global_obj.side_bar_all_items_obj().click()
        self.global_obj.hamburger_menu_obj().click()
        self.global_obj.side_bar_reset_app_state_obj().click()

        self.standard_user.first_add_to_cart_button_obj().click()
        self.standard_user.second_add_to_cart_button_obj().click()

        self.global_obj.cart_button_obj().click()

    def test_second_product_title_name(self):
        self.standard_user.second_product_info()
        self.standard_user.second_product_expect_text()

        assert (
                self.standard_user.actual_second_product["second_product_title"]
                == self.standard_user.second_product_title_expect)

    def test_second_product_description(self):
        self.standard_user.second_product_info()
        self.standard_user.second_product_expect_text()

        assert (
                self.standard_user.actual_second_product["second_product_description"]
                == self.standard_user.second_product_description_expect)

    def test_second_product_price(self):
        self.standard_user.second_product_info()
        self.standard_user.second_product_expect_text()

        assert (
                self.standard_user.actual_second_product["second_product_price"]
                == self.standard_user.second_product_price_expect)


    def test_second_remove_button(self):
        self.standard_user.second_product_info()
        self.standard_user.second_product_expect_text()

        assert (
                self.standard_user.actual_second_product["second_remove_button"]
                == self.standard_user.second_remove_button_text)

    def test_second_cart_base_ui(self):
        assert self.global_obj.top_logo_text() == "Swag Labs"  # Cart > 로고 명칭 확인
        assert self.global_obj.cart_button_badge_number_obj() == '2'  # Cart > 상단 cart 아이콘 카운트 2 노출 확인
        assert self.cart.cart_your_cart_title() == "Your Cart"  # Cart > Your Cart Title 확인
        assert self.cart.cart_list_qty() == "QTY"  # Cart > List > QTY 명칭 확인
        assert self.cart.cart_list_description() == "Description"  # Cart > List > Description 명칭 확인

        assert self.cart.cart_list_qty_number_1_obj() == "1"  # Cart > List > 첫번째 상품 Qty > 1 노츨 확인
        assert self.cart.cart_list_product_name_1_obj() == "Sauce Labs Backpack"  # Cart > List > Cart에 추가된 상품명 확인
        assert self.cart.cart_list_product_description_1_obj() == "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection."  # Cart > List > Cart에 추가된 상품 Description 확인
        assert self.cart.cart_list_product_price_1_obj() == "$29.99"  # Cart > List > Cart에 추가된 상품 가격 확인

        assert self.cart.cart_list_qty_number_2_obj() == "1"  # Cart > List > 2번째 상품 Qty > 1 노츨 확인
        assert self.cart.cart_list_product_name_2_obj() == "Sauce Labs Bike Light"  # Cart > List > Cart에 추가된 상품명 확인
        assert self.cart.cart_list_product_description_2_obj() == "A red light isn't the desired state in testing but it sure helps when riding your bike at night. Water-resistant with 3 lighting modes, 1 AAA battery included."  # Cart > List > Cart에 추가된 상품 Description 확인
        assert self.cart.cart_list_product_price_2_obj() == "$9.99"

        assert self.cart.cart_remove_button_text() == "Remove"  # Cart > Remove 버튼 확인
        assert self.cart.cart_continue_shopping_button_text() == "Continue Shopping"  # Cart > Continue 버튼 확인
        assert self.cart.cart_checkout_button_text() == "Checkout"  # Cart > Continue 버튼 확인