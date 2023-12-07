from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


# класс поиска локаторов
class TestSearchLocators:
    #  — локатор поля ввода логина
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    # — локатор поля ввода пароля
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    # — локатор кнопки логина
    LOCATOR_LOGIN_BTN = (By.XPATH, """//*[@id="login"]/div[3]/button""")
    # — локатор поля с ошибкой
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    #  локатор проверки что залогинились - проверка наличия слова BLOG на странице
    LOCATOR_RESULT_LOGIN = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")

    # локатор кнопки создания нового поста
    LOCATOR_CREATE_NEW_POST = (By.XPATH, """//*[@id="create-btn"]""")
    # локатор поля - ввести название поста
    LOCATOR_POST_TITLE = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    # локатор поля - ввести содержание поста
    LOCATOR_POST_CONTENT = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    # локатор кнопки создания/сохраниения поста
    LOCATOR_CREATE_POST_BTN = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button""")
    # локатор проверки создания нового поста - проверка на наличие слов- название поста
    LOCATOR_POST = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")


    # локатор кнопки Contact
    LOCATOR_BTN_CONTACT = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    # локатор проверки открытие формы Contact
    LOCATOR_RESULT_SWITCHIHG_TO_FORM = (By.XPATH, """//*[@id="app"]/main/div/div/h1""")
    # локатор поля your name
    LOCATOR_FIELD_YOUR_NAME = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    # локатор поля your email
    LOCATOR_FIELD_YOUR_EMAIL = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    # локатор поля content в форме Contact
    LOCATOR_FIELD_CONTENT_TO_FORM = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    # локатор кнопки contact us
    LOCATOR_BTN_CONTACT_US = (By.XPATH, """//*[@id="contact"]/div[4]/button""")



# класс с методами (действиями с локаторами из файла test_1)

class OperationsHelper(BasePage):
    #  функция ввода логина
    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    #  функция ввода пароля
    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    #  функция нажатия кнопки login
    def click_login_button(self):
        logging.info(f"Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    #  функция вывода  текста (в нашем случае 401)
    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=2)
        text = error_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text

    # функция поиска слова blog
    def get_text_blog(self):
        text_field = self.find_element(TestSearchLocators.LOCATOR_RESULT_LOGIN, time=2)
        text = text_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_RESULT_LOGIN[1]}")
        return text

    # функция нажатия на кнопку создания нового поста
    def click_nwe_post_button(self):
        logging.info(f"Click new post button")
        self.find_element(TestSearchLocators.LOCATOR_CREATE_NEW_POST).click()

    # функция ввода названия поста в поле
    def enter_title_post(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_POST_TITLE[1]}")
        title_field = self.find_element(TestSearchLocators.LOCATOR_POST_TITLE)
        title_field.clear()
        title_field.send_keys(word)

    # функция ввода содержимого поста в поле
    def enter_content_post(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_POST_CONTENT[1]}")
        content_field = self.find_element(TestSearchLocators.LOCATOR_POST_CONTENT)
        content_field.clear()
        content_field.send_keys(word)

    # функция нажатия кнопки создания/сохранения поста
    def click_create_nwe_post_button(self):
        logging.info(f"Click new post button")
        self.find_element(TestSearchLocators.LOCATOR_CREATE_POST_BTN).click()

    # функция проверки наличия созданоого поста- наличие названия поста
    def post(self):
        post_field = self.find_element(TestSearchLocators.LOCATOR_POST, time=2)
        text = post_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_POST[1]}")
        return text

    #  функция нажатия кнопки Contact
    def click_сontact_button(self):
        logging.info(f"Click сontact button")
        self.find_element(TestSearchLocators.LOCATOR_BTN_CONTACT).click()

    #     функция проверки открытия формы- наличие слов Contact us!
    def result_switcying_to_form_text(self):
        result_field = self.find_element(TestSearchLocators.LOCATOR_RESULT_SWITCHIHG_TO_FORM, time=2)
        text = result_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_RESULT_SWITCHIHG_TO_FORM[1]}")
        return text

    # функция ввода имени в поле your name
    def enter_name(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_FIELD_YOUR_NAME[1]}")
        name_field = self.find_element(TestSearchLocators.LOCATOR_FIELD_YOUR_NAME)
        name_field.clear()
        name_field.send_keys(word)

    #  функция ввода email в поле your email
    def enter_email(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_FIELD_YOUR_EMAIL[1]}")
        name_field = self.find_element(TestSearchLocators.LOCATOR_FIELD_YOUR_EMAIL)
        name_field.clear()
        name_field.send_keys(word)

    #  функция ввода содержимого в поле content
    def enter_content_to_form(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_FIELD_CONTENT_TO_FORM[1]}")
        content_field = self.find_element(TestSearchLocators.LOCATOR_FIELD_CONTENT_TO_FORM)
        content_field.clear()
        content_field.send_keys(word)

    # функция нажатия кнопки contact us
    def click_contact_us_button(self):
        logging.info(f"Click login button")
        self.find_element(TestSearchLocators.LOCATOR_BTN_CONTACT_US).click()

    #  функция вывода  текста в alert -  Form successfully submitted
    def get_alert_text(self):
        alert_field = self.driver.switch_to.alert
        text = alert_field.text
        logging.info(f"We find text {text} in alert")
        return text

