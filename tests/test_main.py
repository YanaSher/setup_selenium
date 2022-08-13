from page_objects.main_page import MainPage

def test_main_page_external(browser):
    assert "Your Store" == browser.title #проверяем титл страницы на соответствие
    main_page = MainPage(browser)
    main_page.verify_top_menu()
    main_page.verify_input_search()
    main_page.verify_button_search()
    main_page.verify_button_basket()
    main_page.verify_logo()

