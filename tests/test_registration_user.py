from page_objects.locators.registration_user_locator import RegistrationUserLocator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# поиск элементов на страницерегистрации пользователя
def test_catalog_page_external(browser):
    browser.find_element(*RegistrationUserLocator.MI_ACCOUNT).click()
    browser.find_element(*RegistrationUserLocator.REGISTER_LINK).click()
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(RegistrationUserLocator.HEADER_TEXT))
    browser.find_element(*RegistrationUserLocator.FIRST_NAME_INPUT)
    browser.find_element(*RegistrationUserLocator.LAST_NAME_INPUT)
    browser.find_element(*RegistrationUserLocator.EMAIL_INPUT)
    browser.find_element(*RegistrationUserLocator.TELEPHONE_INPUT)
    browser.find_element(*RegistrationUserLocator.PASSWORD_INPUT)
    browser.find_element(*RegistrationUserLocator.CONFIRM_PASSWORD_INPUT)
    browser.find_element(*RegistrationUserLocator.CHECK_BOX_POLICY)
    browser.find_element(*RegistrationUserLocator.POLICY_LINK)
    browser.find_element(*RegistrationUserLocator.CONTINUE_BUTTON)
