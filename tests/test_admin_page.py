from page_objects.locators.login_admin_page_locator import LoginAdminPage


# поиск элементов на странице входа в админку
def test_login_page_external(browser):
    browser.get(browser.url + "/admin")
    browser.find_element(*LoginAdminPage.USERNAME_INPUT)
    browser.find_element(*LoginAdminPage.PASSWORD_INPUT)
    browser.find_element(*LoginAdminPage.SUBMIT_BUTTON)
    browser.find_element(*LoginAdminPage.FORGOTTEN_PASSWORD)
    browser.find_element(*LoginAdminPage.OPENCART_LINK)