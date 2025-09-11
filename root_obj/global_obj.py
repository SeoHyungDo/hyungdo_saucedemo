from http.client import responses
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.support.wait import WebDriverWait


class global_menu:
    def __init__(self, driver):  # 생성자, 객체를 생성할 때 driver객체를 인자로 넣어 줄 것이라 생각하고 그 driver 객체를 받아 self.driver에 할당
        self.driver = driver

    # 버튼 액션과 명칭 검증 등 여러가지가 필요한 경우 변수로 선언 했습니다.
    top_logo = (By.XPATH,'//*[@id="header_container"]/div[1]/div[2]/div')
    hamburger_menu = (By.CLASS_NAME, 'bm-burger-button')
    side_bar_all_items = (By.XPATH,'//*[@id="inventory_sidebar_link"]')
    side_bar_about = (By.XPATH, '//*[@id="about_sidebar_link"]')
    side_bar_logout = (By.XPATH, '//*[@id="logout_sidebar_link"]')
    twitter_button = (By.XPATH,'//*[@id="page_wrapper"]/footer/ul/li[1]/a')
    facebook_button = (By.XPATH, '//*[@id="page_wrapper"]/footer/ul/li[2]/a')
    instagram_button = (By.XPATH, '//*[@id="page_wrapper"]/footer/ul/li[3]/a')
    side_bar_reset_app_state = (By.XPATH, '//*[@id="reset_sidebar_link"]')
    side_bar_x_button = (By.XPATH, '//*[@id="react-burger-cross-btn"]')
    cart_button = (By.XPATH, '//*[@id="shopping_cart_container"]/a')
    cart_button_badge = (By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    cart_button_badge_number = (By.XPATH, '//*[@id="shopping_cart_container"]/a/span')

    def top_logo_obj(self):
        return self.driver.find_element(*self.top_logo)

    def top_logo_text(self) :
        return self.driver.find_element(*self.top_logo).text

    def hamburger_menu_obj(self) :
        return self.driver.find_element(*self.hamburger_menu)

    def side_bar_all_items_obj(self):
        return self.driver.find_element(*self.side_bar_all_items)

    def side_bar_all_items_text(self):
        return self.driver.find_element(*self.side_bar_all_items).text

    def side_bar_about_obj(self):
        return self.driver.find_element(*self.side_bar_about)

    def side_bar_about_text(self):
        return self.driver.find_element(*self.side_bar_about).text

    def side_bar_logout_obj(self):
        return self.driver.find_element(*self.side_bar_logout)

    def side_bar_logout_text(self):
        return self.driver.find_element(*self.side_bar_logout).text

    def side_bar_reset_app_state_obj(self):
        return self.driver.find_element(*self.side_bar_reset_app_state)

    def side_bar_reset_app_text(self):
        return self.driver.find_element(*self.side_bar_reset_app_state).text

    def side_bar_x_button_obj(self):
        return self.driver.find_element(*self.side_bar_x_button)

    def cart_button_obj(self):
        return self.driver.find_element(*self.cart_button)

    def cart_button_badge_obj(self):
        return self.driver.find_element(*self.cart_button_badge)

    def cart_button_badge_number_obj(self):
        return self.driver.find_element(*self.cart_button_badge_number).text

    def twitter_button_obj(self):
        return self.driver.find_element(*self.twitter_button)

    def facebook_button_obj(self):
        return self.driver.find_element(*self.facebook_button)

    def instagram_button_obj(self):
        return self.driver.find_element(*self.instagram_button)

    def twitter_button_tab_action(self):
        tabs = self.driver.window_handles # 현재 열려있는 탭 리스트 확인
        self.driver.switch_to.window(tabs[-1]) # 새 탭으로 전환 (보통 마지막 index가 새 탭)
        new_tab_twitter_url = self.driver.current_url # URL 받아서 저장
        self.driver.close() # 탭 닫기
        self.driver.switch_to.window(tabs[0]) # 원래 탭으로 돌아오기 (첫 번째 탭)
        return new_tab_twitter_url # URL 리턴

    def facebook_button_tab_action(self):
        tabs = self.driver.window_handles # 현재 열려있는 탭 리스트 확인
        self.driver.switch_to.window(tabs[-1]) # 새 탭으로 전환 (보통 마지막 index가 새 탭)
        new_tab_facebook_url = self.driver.current_url # URL 받아서 저장
        self.driver.close() # 탭 닫기
        self.driver.switch_to.window(tabs[0]) # 원래 탭으로 돌아오기 (첫 번째 탭)
        return new_tab_facebook_url # URL 리턴

    def linkedin_button_tab_action(self):
        original_window = self.driver.current_window_handle
        self.linkedin_button_obj().click()

        # 새 탭 열릴 때까지 대기
        WebDriverWait(self.driver, 5).until(lambda d: len(d.window_handles) > 1)
        new_window = [w for w in self.driver.window_handles if w != original_window][0]

        self.driver.switch_to.window(new_window)
        linkedin_url = self.driver.current_url
        self.driver.close()  # 새 탭 닫기

        # 원래 탭이 살아있으면 돌아가기
        if original_window in self.driver.window_handles:
            self.driver.switch_to.window(original_window)
        else:
            raise Exception("원래 탭이 닫혀있어 복귀할 수 없습니다.")

        return linkedin_url