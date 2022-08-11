from urllib import request
import os
import pytest
from selenium import webdriver
from selenium.webdriver.opera.options import Options as OperaOptions


# DRIVER = "~/Drivers/"
# DRIVER = "/home/lin/Drivers/"


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
    #    elif browser_name == "opera":
    #        options = OperaOptions()
    #        options.binary_location = r"/snap/bin/opera"
    #        browser = webdriver.Opera(executable_path=f"{drivers}/operadriver", options=options)
    #    elif browser_name == "opera2":
    #        ChromeDriverService service = new ChromeDriverService.Builder().usingDriverExecutable(new File(f"{drivers}/operadriver")).build();
    #        ChromeDriver driver = new ChromeDriver(service);
    #        driver.get("http://selenium2.ru/");
    #        driver.quit();
    else:
        raise ValueError("Browser not supported!")

    driver.maximize_window()
    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver
