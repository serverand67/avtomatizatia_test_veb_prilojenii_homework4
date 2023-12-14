from testpage import OperationsHelper
import logging
import yaml
import time

with open(r"C:\Users\NiKa\PycharmProjects\avtomatizatia_test_veb_prilojenii\lesson4\testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step1(browser):
    logging.info("Test1 starting")
    testpage = OperationsHelper(browser, testdata['address'])
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"


def test_step2(browser):
    logging.info("Test2 starting")
    testpage = OperationsHelper(browser, testdata['address'])
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_button()
    assert testpage.get_text_blog() == "Blog"


def test_step3(browser):
    # залогинится
    logging.info("Test3 starting")
    testpage = OperationsHelper(browser, testdata['address'])
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_button()

    # создания поста
    testpage.click_nwe_post_button()
    testpage.enter_title_post("new title")
    testpage.enter_content_post("content")
    testpage.click_create_nwe_post_button()

    time.sleep(3)

    # Проверка наличия названия поста на странице
    assert testpage.post() == "new title"


def test_step4(browser):
    logging.info("Test4 starting")
    testpage = OperationsHelper(browser, testdata['address'])
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_button()
    testpage.click_сontact_button()
    time.sleep(2)
    assert testpage.result_switcying_to_form_text() == "Contact us!"


#  моя функция перехода на форму Contact, написания сообшения
#  и вывода алерта
def test_step5(browser, send_email):
    # залогинится
    logging.info("Test5 starting")
    testpage = OperationsHelper(browser, testdata['address'])
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_button()

    # переход на форму
    testpage.click_сontact_button()

    # заполнение полей формы
    testpage.enter_name("name")
    testpage.enter_email("email@email.ru")
    testpage.enter_content_to_form("content")
    testpage.click_contact_us_button()

    time.sleep(3)

    # Проверка наличия надписи - Form successfully submitted - в alert
    assert testpage.get_alert_text() == "Form successfully submitted"

