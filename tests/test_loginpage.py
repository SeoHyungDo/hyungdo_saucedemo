import pytest
import time
import requests
from selenium.webdriver.common.by import By
from utility.passclass import passclass
from root_obj.loginpage_obj import saucedemo_home
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from root_obj.global_obj import global_menu

class Test_demotest(passclass) :

    # URL로 정상 연결 되는지 확인한다.
    def test_login_url_check(self):
        url = "https://www.saucedemo.com/"
        try:
           responses = requests.get(url, timeout=10)
           assert responses.status_code == 200

        except requests.exceptions.RequestException as e:
           pytest.fail(f"url 접속 실패 : {e}")

    # 상단 로고 텍스트가 정상 노출되는지 확인한다.
    def test_login_top_logo(self) :
        saucedemo = saucedemo_home(self.driver)
        assert saucedemo.login_top_logo_text() == "Swag Labs"

    # locked 계정 Validation 노출 결과를 확인한다.
    def test_lock_validation(self) :
        saucedemo = saucedemo_home(self.driver)
        expected_text = "Epic sadface: Sorry, this user has been locked out."
        saucedemo.input_id_standard_user_login_obj("locked_out_user","secret_sauce") #standard User Login
        validation_text_area_text = saucedemo.validation_text_area_obj().text
        assert expected_text == validation_text_area_text

    # ID / 비밀번호 불일치 Validation을 확인한다
    def test_id_pw_invaild_validation(self) :
        saucedemo = saucedemo_home(self.driver)
        saucedemo.id_pw_clear()

        expected_text = "Epic sadface: Username and password do not match any user in this service"
        saucedemo.input_id_standard_user_login_obj("locked_out_user","1234") #standard User Login
        validation_text_area_text = saucedemo.validation_text_area_obj().text
        assert expected_text == validation_text_area_text

    # ID / 비밀번호 미 입력
    def test_id_pw_not_exist_validation(self) :
        saucedemo = saucedemo_home(self.driver)
        saucedemo.id_pw_clear()

        expected_text = "Epic sadface: Username is required"
        saucedemo.input_id_standard_user_login_obj("","") #standard User Login
        validation_text_area_text = saucedemo.validation_text_area_obj().text
        assert expected_text == validation_text_area_text

    # 로그인 후 URL에 inventory.html이 있는지 확인한다.
    def test_input_id(self) :
        saucedemo = saucedemo_home(self.driver)
        saucedemo.id_pw_clear()

        saucedemo.input_id_standard_user_login_obj("standard_user","secret_sauce") #standard User Login

        wait = WebDriverWait(self.driver, 10)
        inventory_container = wait.until(
            EC.presence_of_element_located((By.ID, "inventory_container"))
        )
        assert "inventory.html" in self.driver.current_url


# time.sleep(10)
#    def test_apply_store_selectbox_action(self):
#        Coupang_main = coupang_main(self.driver)
#        expected_text = "오픈마켓\n여행·티켓\n로켓배송\n제휴마케팅\n로켓그로스"
#        Coupang_main.apply_store_select_box_obj().click()
#        apply_store_select_box_data = Coupang_main.apply_store_select_box_data_obj()
#        for select_box_text in apply_store_select_box_data :
#            apply_store_select_box_text = select_box_text.text
#        assert apply_store_select_box_text == expected_text
