from page_objects.base_page import BasePage
from page_objects.locators.product_page_locator import ProductPageLocator


class ProductPage(BasePage):
    path = "/camera/nikon-d300"

    def open(self, url):
        self.browser.get(url + self.path)

    def verify_header_product(self):
        self.verify_element_presence(ProductPageLocator.HEADER_PRODUCT)

    def verify_add_button(self):
        self.verify_element_presence(ProductPageLocator.ADD_BUTTON)

    def verify_product_price(self):
        self.verify_element_presence(ProductPageLocator.PRODUCT_PRICE)

    def verify_twit_link(self):
        self.verify_element_presence(ProductPageLocator.TWIT_LINK)

    def verify_count_input(self):
        self.verify_element_presence(ProductPageLocator.COUNT_INPUT)