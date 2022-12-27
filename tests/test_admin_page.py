from page_objects.admin_page import AdminPage


# поиск элементов на странице входа в админку
def test_login_page_external(browser, url):
    admin_page = AdminPage(browser)
    admin_page.open(url)
    admin_page.verify_user_input()
    admin_page.verify_password_input()
    admin_page.verify_submit_button()
    admin_page.verify_forgotten_pasword()
    admin_page.verify_opencart_link()


def test_login_admin(browser, url):
    admin_page = AdminPage(browser)
    admin_page.open(url)
    admin_page.login_admin("user", "bitnami")
