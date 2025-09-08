import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#반복 사용할 유틸리티 생성
@pytest.mark.usefixtures("setup")
class BaseClass :

    def explicit_wait_text(self, text): #명시적 대기를 압축
        element = WebDriverWait(self.driver,10).until(
        EC.presense_of_element_located((By.LINK_TEXT, text))) # 메소드 일반화, TC에서 텍스트를 받아 옴
        # 수행할 TC에서 self.explicit_wait("텍스트")를 입력한다

    def explicit_wait_selectbox(self): #명시적 대기를 압축
        element = WebDriverWait(self.driver,10).until(
        EC.presense_of_element_located((By.XPATH, '//*[@id="subscribeHeader"]/li[2]/a')))