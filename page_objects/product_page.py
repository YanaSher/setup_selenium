import allure

from page_objects.base_page import BasePage
from page_objects.locators.product_page_locator import ProductPageLocator


class ProductPage(BasePage):
    path = "/camera/nikon-d300"

    @allure.step("Открытие продукта nikon-d300")
    def open(self, url):
        self.browser.get(url + self.path)

    @allure.step("Проверка того, что открылась нужная страница")
    def verify_header_product(self):
        self.verify_element_presence(ProductPageLocator.HEADER_PRODUCT)

    @allure.step("Проверка наличия кнопки добавления товара в корзину")
    def verify_add_button(self):
        self.verify_element_presence(ProductPageLocator.ADD_BUTTON)

    @allure.step("Проверка наличия цены")
    def verify_product_price(self):
        self.verify_element_presence(ProductPageLocator.PRODUCT_PRICE)

    @allure.step("Проверка наличия ссылки на твиттер")
    def verify_twit_link(self):
        self.verify_element_presence(ProductPageLocator.TWIT_LINK)

    @allure.step("Проверка наличия поле ввода кол-ва продуктов")
    def verify_count_input(self):
        self.verify_element_presence(ProductPageLocator.COUNT_INPUT)
