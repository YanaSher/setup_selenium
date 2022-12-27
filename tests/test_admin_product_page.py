from page_objects.admin_product_page import AdminProductPage
from page_objects.admin_page import AdminPage
from page_objects.elements.admin_navigator_menu import AdminNavigatorMenu


def test_add_product(browser, url):
    admin_product_page = AdminPage(browser)
    admin_product_page.open(url)
    admin_product_page.login_admin("user", "bitnami")
    admin_product_page = AdminNavigatorMenu(browser)
    admin_product_page.click_catalog_menu()
    admin_product_page.click_product_catalog()
    admin_product_page.open_products_catalog()
    admin_product_page = AdminProductPage(browser)
    admin_product_page.click_add_product_button()
    admin_product_page.input_product_name()
    admin_product_page.input_meta_tag_title()
    admin_product_page.click_tab_data()
    admin_product_page.input_model()
    admin_product_page.click_save_button()
    admin_product_page.verify_success_message()


def test_delete_product(browser, url):
    test_add_product(browser, url)
    admin_product_page = AdminProductPage(browser)
    admin_product_page.find_product_name()
    admin_product_page.click_filter_button()
    admin_product_page.click_check_box()
    admin_product_page.click_delete_product_button()
    admin_product_page.alert_delete_product(browser)
