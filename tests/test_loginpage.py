import pytest
import time
from selenium.webdriver.common.by import By
from utility.passclass import passclass
from root_obj.homepage_obj import saucedemo_home
from utility.BaseClass import BaseClass

class Test_demotest(passclass) :

    def test_login_logo(self) :
        saucedemo = saucedemo_home(self.driver)
        login_logo_text = saucedemo.login_logo_obj().text
        assert login_logo_text == "Swag Labs"


#    def test_apply_store_selectbox_action(self):
#        Coupang_main = coupang_main(self.driver)
#        expected_text = "오픈마켓\n여행·티켓\n로켓배송\n제휴마케팅\n로켓그로스"
#        Coupang_main.apply_store_select_box_obj().click()
#        apply_store_select_box_data = Coupang_main.apply_store_select_box_data_obj()
#        for select_box_text in apply_store_select_box_data :
#            apply_store_select_box_text = select_box_text.text
#        assert apply_store_select_box_text == expected_text
