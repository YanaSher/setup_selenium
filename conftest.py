import datetime
import os
import pytest
import logging
from selenium import webdriver


# довляем возможность выбирать браузер и папку с драйверами и адресс в командной строке
def pytest_addoption(parser):
    parser.addoption("--browser", default="MicrosoftEdge")
    parser.addoption("--drivers", default=os.path.expanduser("~/Drivers"))
    parser.addoption("--url", action="store", default="http://192.168.0.207:8081/")
    parser.addoption("--log_level", action="store", default="DEBUG")
    parser.addoption("--executor", action="store", default="172.17.0.1")
    parser.addoption("--bv")
    parser.addoption("--vnc", action="store_true", default=True)
    parser.addoption("--videos", action="store_true", default=False)


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    drivers = request.config.getoption("--drivers")
    url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bv")
    vnc = request.config.getoption("--vnc")
    videos = request.config.getoption("--videos")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test {} started at {}".format(request.node.name, datetime.datetime.now()))

    if executor == "local":

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
    else:
        executor_url = f"http://{executor}:4444/wd/hub"

        capabilities = {
            "browserName": browser_name,
            "browserVersion": version,
            "name": "opencart",
            "selenoid:options": {
                "enableVNC": vnc,
                "enableVideo": videos
            }
        }
        driver = webdriver.Remote(command_executor=executor_url, desired_capabilities=capabilities)
        driver.maximize_window()

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    def fin():
        driver.quit()
        logger.info("===> Test {} finished at {}".format(request.node.name, datetime.datetime.now()))

    request.addfinalizer(fin)

    driver.get(url)
    driver.url = url

    return driver
