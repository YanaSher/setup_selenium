import os
import pytest
from selenium import webdriver


# довляем возможность выбирать браузер и папку с драйверами и адресс в командной строке
def pytest_addoption(parser):
    parser.addoption("--browser", default="firefox")
    parser.addoption("--drivers", default=os.path.expanduser("~/Drivers"))
    parser.addoption("--url", action="store", default="http://192.168.0.207:8081/")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    drivers = request.config.getoption("--drivers")
    url = request.config.getoption("--url")
    if browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=f"{drivers}/geckodriver")
    elif browser_name == "chrome":
        driver = webdriver.Chrome(executable_path=f"{drivers}/chromedriver")
    elif browser_name == "edge":
        driver = webdriver.Edge(executable_path=f"{drivers}/msedgedriver")
    elif browser_name == "opera":
        driver = webdriver.Opera(executable_path=f"{drivers}/operadriver")
    else:
        raise ValueError("Browser not supported!")

    driver.maximize_window()
    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver
