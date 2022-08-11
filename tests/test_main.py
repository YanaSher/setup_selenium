from page_objects.locators.main_page_locator import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_main_page_external(browser):
    assert "Your Store" == browser.title #проверяем титл страницы на соответствие
    browser.find_element(*MainPageLocators.TOP_MENU) #проверяем верхне меню на наличие
    browser.find_element(*MainPageLocators.INPUT_SEARCH) #проверяем поисковое полле ввода на наличие
    browser.find_element(*MainPageLocators.BUTTON_SEARCH) #проверяем кнопку поиска на наличие
    browser.find_element(*MainPageLocators.BASKET_BUTTON) #проверяю большую кнопку корзины

#проверка кнопоки с валютами c использованием явного ожидания
def test_main_page_valut(browser):
    btn = browser.find_element(*MainPageLocators.FORM_CURRENCY)
    btn.click()
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(MainPageLocators.EURO_CURRENCY))
