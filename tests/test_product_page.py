from page_objects.locators.product_page_locator import ProductPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# поиск элементов на странице входа в админку
def test_product_page_external(browser):
    browser.get(browser.url + "/camera/nikon-d300")
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(ProductPage.HEADER_PRODUCT))
    browser.find_element(*ProductPage.ADD_BUTTON)
    browser.find_element(*ProductPage.PRODUCT_PRICE)
    browser.find_element(*ProductPage.TWIT_LINK)
    browser.find_element(*ProductPage.COUNT_INPUT)
