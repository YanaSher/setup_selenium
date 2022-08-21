from page_objects.registration_user_page import RegistrationUserPage


# поиск элементов на странице регистрации пользователя
def test_catalog_page_external(browser):
    registration_user_page = RegistrationUserPage(browser)
    registration_user_page.transition_to_Registration_User()
    registration_user_page.verify_header()
    registration_user_page.verify_first_name_input()
    registration_user_page.verify_last_name_input()
    registration_user_page.verify_email_input()
    registration_user_page.verify_telephone_input()
    registration_user_page.verify_password_input()
    registration_user_page.verify_confirm_password_input()
    registration_user_page.verify_check_box_policy()
    registration_user_page.verify_policy_link()
    registration_user_page.veify_continue_button()


# регистрация пользователя
def test_registration_new_user(browser):
    registration_user_page = RegistrationUserPage(browser)
    registration_user_page.transition_to_Registration_User()
    registration_user_page.input_first_name()
    registration_user_page.input_last_name()
    registration_user_page.input_email()
    registration_user_page.input_telephone()
    registration_user_page.input_password("test")
    registration_user_page.input_confirm_password("test")
    registration_user_page.click_check_box()
    registration_user_page.click_button_continue()
