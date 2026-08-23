import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from root_obj.global_obj import global_menu
from root_obj.standard_user_obj import standard_user_obj
from root_obj.cart_obj import cart


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")

    chrome_option = webdriver.ChromeOptions()

    chrome_option.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    })

    chrome_option.add_argument("--disable-save-password-bubble")
    chrome_option.add_argument("--disable-password-manager-reauthentication")
    chrome_option.add_argument("--disable-infobars")

    if browser_name == "chrome":
        driver = webdriver.Chrome(options=chrome_option)

    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    else:
        raise ValueError(f"지원하지 않는 브라우저: {browser_name}")

    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)

    request.cls.driver = driver
    request.cls.global_obj = global_menu(driver)
    request.cls.standard_user = standard_user_obj(driver)
    request.cls.cart = cart(driver)

    yield

    driver.quit()


@pytest.fixture(scope="function")
def setup_function(request):
    browser_name = request.config.getoption("browser_name")
    driver = None

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

    else:
        raise ValueError(f"지원하지 않는 브라우저: {browser_name}")

    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)

    request.cls.driver = driver

    yield driver

    if driver:
        driver.quit()