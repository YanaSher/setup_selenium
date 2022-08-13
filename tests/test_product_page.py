from page_objects.product_page import ProductPage


# поиск элементов на странице входа в админку
def test_product_page_external(browser, url):
    product_page = ProductPage(browser)
    product_page.open(url)
    product_page.verify_header_product()
    product_page.verify_add_button()
    product_page.verify_product_price()
    product_page.verify_twit_link()
    product_page.verify_count_input()

