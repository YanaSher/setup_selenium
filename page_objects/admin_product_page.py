import allure

from randomaizer import random_string
from page_objects.base_page import BasePage
from page_objects.locators.admin_producte_page_locator import AdminProductePageLocator


class AdminProductPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.text_name = "NjaiFas"

    @allure.step("Нажатие кнопки - добавление продукта")
    def click_add_product_button(self):
        self.click_element(AdminProductePageLocator.ADD_PRODYCT_BUTTON)

    @allure.step("Ввод имени продукта")
    def input_product_name(self):
        self.input_text(AdminProductePageLocator.INPUT_PRODUCT_NAME, self.text_name)

    @allure.step("Ввод Meta Tag Title")
    def input_meta_tag_title(self):
        self.input_text(AdminProductePageLocator.INPUT_MEGA_TAG_TITLE, random_string(8))

    @allure.step("Переход на вкладку DATA")
    def click_tab_data(self):
        self.click_element(AdminProductePageLocator.DATA_TAB)

    @allure.step("Ввод Input Model")
    def input_model(self):
        self.input_text(AdminProductePageLocator.INPUT_MODEL, random_string(5))

    @allure.step("Сохранение данных нового продукта")
    def click_save_button(self):
        self.click_element(AdminProductePageLocator.SAVE_BUTTON)

    @allure.step("Проверка сообщения о том, что продукт создан успешно")
    def verify_success_message(self):
        success_message = self.get_text(AdminProductePageLocator.SUCCESS_MESSAGE)
        success_message = success_message[:-2]
        assert success_message == "Success: You have modified products!"

    @allure.step("Ввод в фильтр")
    def find_product_name(self):
        self.input_text(AdminProductePageLocator.INPUT_PRODUCT_NAME_IN_FILTER, self.text_name)

    @allure.step("Активация фильтровки продуктов")
    def click_filter_button(self):
        self.click_element(AdminProductePageLocator.BUTTON_FILTER)

    @allure.step("Помечаем нужный продукт")
    def click_check_box(self):
        self.click_element(AdminProductePageLocator.CHECK_BOX_IN_PRODUCT_TABLE)

    @allure.step("Удаляем продукт")
    def click_delete_product_button(self):
        self.click_element(AdminProductePageLocator.DELETE_PRODUCT_BUTTON)
