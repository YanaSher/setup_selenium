from page_objects.admin_system_page import AdminSystemPage
from page_objects.admin_page import AdminPage
from page_objects.elements.admin_navigator_menu import AdminNavigatorMenu

def test_add_user(browser, url):
    admin_system_page = AdminPage(browser)
    admin_system_page.open(url)
    admin_system_page.login_admin("user", "bitnami")
    admin_system_page = AdminNavigatorMenu(browser)
    admin_system_page.open_users_catalog()
    admin_system_page = AdminSystemPage(browser)
    admin_system_page.click_add_user_button()
    admin_system_page.input_user_name("1 test")
    admin_system_page.choise_user_group_demonstration()
    admin_system_page.input_first_name()
    admin_system_page.input_last_name()
    admin_system_page.input_email()
    admin_system_page.input_password("test")
    admin_system_page.input_confirm_password("test")
    admin_system_page.choise_status_enabled()
    admin_system_page.click_save_button()
    admin_system_page.verify_success_message()

def test_dont_created_user_with_the_same_name(browser,url):
    admin_system_page = AdminPage(browser)
    admin_system_page.open(url)
    admin_system_page.login_admin("user", "bitnami")
    admin_system_page = AdminNavigatorMenu(browser)
    admin_system_page.open_users_catalog()
    admin_system_page = AdminSystemPage(browser)
    admin_system_page.click_add_user_button()
    admin_system_page.input_user_name("1 test")
    admin_system_page.choise_user_group_demonstration()
    admin_system_page.input_first_name()
    admin_system_page.input_last_name()
    admin_system_page.input_email()
    admin_system_page.input_password("test")
    admin_system_page.input_confirm_password("test")
    admin_system_page.choise_status_enabled()
    admin_system_page.click_save_button()
    admin_system_page.warning_success_message()
    admin_system_page.click_cancel_delete_user_button()
    admin_system_page.click_check_box("1 test")
    admin_system_page.click_delete_user_button()
    admin_system_page.alert_delete_product(browser)



def test_delete_product(browser, url):
    admin_system_page = AdminPage(browser)
    admin_system_page.open(url)
    admin_system_page.login_admin("user", "bitnami")
    admin_system_page = AdminNavigatorMenu(browser)
    admin_system_page.open_users_catalog()
    admin_system_page = AdminSystemPage(browser)
    admin_system_page.click_add_user_button()
    admin_system_page.input_user_name("2 test")
    admin_system_page.choise_user_group_demonstration()
    admin_system_page.input_first_name()
    admin_system_page.input_last_name()
    admin_system_page.input_email()
    admin_system_page.input_password("test")
    admin_system_page.input_confirm_password("test")
    admin_system_page.choise_status_enabled()
    admin_system_page.click_save_button()
    admin_system_page.verify_success_message()
    admin_system_page.click_check_box("2 test")
    admin_system_page.click_delete_user_button()
    admin_system_page.alert_delete_product(browser)
    admin_system_page.verify_success_message()


