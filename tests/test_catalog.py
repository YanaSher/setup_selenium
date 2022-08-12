from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.locators.catalog_page_locator import CatalogPage


# поиск элементов на странице каталога
def test_catalog_page_external(browser):
    browser.get(browser.url + "/camera")
    browser.find_element(*CatalogPage.CATALOG_HEADER)
    browser.find_element(*CatalogPage.HEADER_TEXT)
    browser.find_element(*CatalogPage.LIST_VIEW)
    browser.find_element(*CatalogPage.GREED_VIEW)
    browser.find_element(*CatalogPage.BUTTON_SHOW)
    browser.find_element(*CatalogPage.BUTTON_SORT_BY)


# проверка переключений по товарам
def test_catalog_page_different_product(browser):
    browser.get(browser.url + "/camera")
    browser.find_element(*CatalogPage.BUTTON_DESKTOPS).click()
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(CatalogPage.HEADER_DESKTOPS))
    browser.find_element(*CatalogPage.BUTTON_LAPTOPS_NOTEBOOKS).click()
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(CatalogPage.HEADER_LAPTOPS_NOTEBOOKS))
