import datetime
import os
import pytest
import logging
from selenium import webdriver



# довляем возможность выбирать браузер и папку с драйверами и адресс в командной строке
def pytest_addoption(parser):
    parser.addoption("--browser", default="firefox")
    parser.addoption("--drivers", default=os.path.expanduser("~/Drivers"))
    parser.addoption("--url", action="store", default="http://192.168.0.207:8081/")
    parser.addoption("--log_level", action="store", default="DEBUG")

@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    drivers = request.config.getoption("--drivers")
    url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test {} started at {}".format(request.node.name, datetime.datetime.now()))

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

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

#    logger.info("Browser:{}".format(browser.desired_capabilities))
    driver.maximize_window()

    def fin():
        driver.quit()
        logger.info("===> Test {} finished at {}".format(request.node.name, datetime.datetime.now()))

    request.addfinalizer(fin)

    driver.get(url)
    driver.url = url

    return driver
