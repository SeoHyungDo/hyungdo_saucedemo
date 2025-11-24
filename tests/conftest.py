import json

import pytest
import os
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests
from root_obj.global_obj import global_menu
from root_obj.standard_user_obj import standard_user_obj
from root_obj.cart_obj import cart

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
# 맨 앞 "-- " 부분은 키 변수명 입력 (명령어 맨 앞부분)
# 키에 값을 할당하여 보관하고 싶은 경우 "store"를 action에 넣어 줌
# default 속성 = cmd 등을 통해 크롬 등의 값 전달, 아무 정보도 입력하지 않는 경우 default에 세팅 된 기본 값 받음. 통상 크롬을 사용할 것
# help는 부연 설명으로 필수 아님


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name") # 인자로 옵션 이름을 넣어주면 pytest_addoption에 전달했던 값을 받음

    # service_obj = Service(r"\Users\tjg10\PycharmProjects\PythonProject\Chromedriver.exe")
    # Mac의 경우 Chromedriver만 쓰면 됨, .exe는 윈도우에서 기재
    chrome_option = webdriver.ChromeOptions()
    # 비밀번호 관리자 및 자동 완성을 완전히 비활성화 (가장 중요)
    chrome_option.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False, #2줄은 기본 제공 옵션 알림 끄기
        "profile.password_manager_leak_detection": False # 비밀번호 유출 감지 알림 끄기
    })

    # 브라우저 시작 시 팝업 관련 기능을 비활성화
    chrome_option.add_argument("--disable-save-password-bubble")
    chrome_option.add_argument("--disable-password-manager-reauthentication")
    chrome_option.add_argument("--disable-infobars")

    if browser_name == "chrome" :
        driver = webdriver.Chrome(options=chrome_option)
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
    elif browser_name == "firefox" :
        driver = webdriver.Firefox()
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
    elif browser_name == "IE" :
        print("IE 브라우저 설치시 IE 사용 가능")

    # headless, SSL 오류 패스를 위한 chrome_option 선언
    # driver = webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(5)
    request.cls.driver = driver  # 여기서 선언한 객체가 클래스로 보내짐, 해당 문이 있으면 return 필요 없음
    request.cls.global_obj = global_menu(driver)
    request.cls.standard_user = standard_user_obj(driver)
    request.cls.cart = cart(driver)

    yield  # 테스트 종료 후
    driver.close()  # 브라우저를 닫아줌


@pytest.fixture(scope="function")
def setup_function(request):
    browser_name = request.config.getoption("browser_name")
    driver = None  # 드라이버 객체를 미리 초기화

    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        })
        options.add_argument("--disable-save-password-bubble")
        options.add_argument("--disable-password-manager-reauthentication")
        options.add_argument("--disable-infobars")

        driver = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    if driver:
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        request.cls.driver = driver  # 클래스 내에서 self.driver 로 접근 가능
    yield driver  # driver 객체를 직접 반환합니다.

    # yield 이후 드라이버가 존재할 때만 닫아줌
    if driver:
        driver.quit()