from page_objects.catalog_page import CatalogPage


# поиск элементов на странице каталога
def test_catalog_page_external(browser, url):
    catalog_page = CatalogPage(browser)
    catalog_page.open(url)
    catalog_page.verify_catalog_header()
    catalog_page.verify_header_text()
    catalog_page.verify_list_view()
    catalog_page.verify_greed_view()
    catalog_page.verify_button_show()
    catalog_page.verify_button_sort_by()


# проверка переключений по товарам
def test_catalog_page_different_product(browser, url):
    catalog_page = CatalogPage(browser)
    catalog_page.open(url)
    catalog_page.transition_to_Desktops()
    catalog_page.transition_to_Laptops_and_Notebooks()
