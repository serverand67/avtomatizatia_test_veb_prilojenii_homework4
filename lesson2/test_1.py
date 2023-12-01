import yaml
import time

with open(r"C:\Users\NiKa\PycharmProjects\avtomatizatia_test_veb_prilojenii\lesson2\testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step1(site, log_xpath, pass_xpath, btn_xpath, result_xpath):
    input1 = site.find_element("xpath", log_xpath)
    input1.send_keys("test")
    input2 = site.find_element("xpath", pass_xpath)
    input2.send_keys("test")
    btn = site.find_element("xpath", btn_xpath)
    btn.click()
    err_lable = site.find_element("xpath", result_xpath)
    assert err_lable.text == "401"


def test_step2(site, log_xpath, pass_xpath, btn_xpath, result_login):
    input1 = site.find_element("xpath", log_xpath)
    input1.send_keys(testdata["login"])
    input2 = site.find_element("xpath", pass_xpath)
    input2.send_keys(testdata["password"])
    btn = site.find_element("xpath", btn_xpath)
    btn.click()
    login = site.find_element("xpath", result_login)
    assert login.text == "Blog"


def test_step3(site, log_xpath, pass_xpath, btn_xpath, result_login, create_new_post_btn_xpath,
               post_title_xpath, post_content_xpath, create_post_btn_xpath, post_xpath):
    # залогинится
    input1 = site.find_element("xpath", log_xpath)
    input1.send_keys(testdata["login"])
    input2 = site.find_element("xpath", pass_xpath)
    input2.send_keys(testdata["password"])
    btn = site.find_element("xpath", btn_xpath)
    btn.click()
    login = site.find_element("xpath", result_login)
    assert login.text == "Blog"

    # создания поста
    create_new_post = site.find_element("xpath", create_new_post_btn_xpath)
    create_new_post.click()

    post_title_input = site.find_element("xpath", post_title_xpath)
    post_title_input.send_keys("Новый пост 1")

    post_content_input = site.find_element("xpath", post_content_xpath)
    post_content_input.send_keys("Содержимое поста.")

    create_post_btn = site.find_element("xpath", create_post_btn_xpath)
    create_post_btn.click()

    time.sleep(3)

    # Проверка наличия названия поста на странице
    created_post = site.find_element("xpath", result_login)
    assert created_post.text == "Новый пост 1"
