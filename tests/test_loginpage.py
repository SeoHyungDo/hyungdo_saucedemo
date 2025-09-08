import pytest
import time
from selenium.webdriver.common.by import By
from utility.passclass import passclass
from root_obj.homepage_obj import saucedemo_home
from utility.BaseClass import BaseClass
import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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
    def test_login_logo(self) :
        saucedemo = saucedemo_home(self.driver)
        login_logo_text = saucedemo.login_logo_obj().text
        assert login_logo_text == "Swag Labs"

    # 로그인 후 URL에 inventory.html이 있는지 확인한다.
    def test_input_id(self) :
        saucedemo = saucedemo_home(self.driver)
        saucedemo.input_id_standard_user_login_obj("standard_user","secret_sauce") #standard User Login

        wait = WebDriverWait(self.driver, 10)
        inventory_container = wait.until(
            EC.presence_of_element_located((By.ID, "inventory_container"))
        )
        assert "inventory.html" in self.driver.current_url

#    def test_apply_store_selectbox_action(self):
#        Coupang_main = coupang_main(self.driver)
#        expected_text = "오픈마켓\n여행·티켓\n로켓배송\n제휴마케팅\n로켓그로스"
#        Coupang_main.apply_store_select_box_obj().click()
#        apply_store_select_box_data = Coupang_main.apply_store_select_box_data_obj()
#        for select_box_text in apply_store_select_box_data :
#            apply_store_select_box_text = select_box_text.text
#        assert apply_store_select_box_text == expected_text
