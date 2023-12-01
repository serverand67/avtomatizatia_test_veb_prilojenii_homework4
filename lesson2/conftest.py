import pytest
from module import Site
import yaml

with open(r"C:\Users\NiKa\PycharmProjects\avtomatizatia_test_veb_prilojenii\lesson2\testdata.yaml") as f:
    testdata = yaml.safe_load(f)


@pytest.fixture()
def log_xpath():
    return """//*[@id="login"]/div[1]/label/input"""


@pytest.fixture()
def pass_xpath():
    return """//*[@id="login"]/div[2]/label/input"""


@pytest.fixture()
def btn_xpath():
    return """//*[@id="login"]/div[3]/button"""


@pytest.fixture()
def result_xpath():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""


@pytest.fixture()
def site():
    my_site = Site(testdata["address"])
    yield my_site
    my_site.close()


@pytest.fixture()
def result_login():
    return """//*[@id="app"]/main/div/div[1]/h1"""

# фикстуры для создания поста
# нажать на кнопку создать пост
@pytest.fixture()
def create_new_post_btn_xpath():
    return """//*[@id="create-btn"]"""

# ввести название поста
@pytest.fixture()
def post_title_xpath():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""

#  ввести содержание поста
@pytest.fixture()
def post_content_xpath():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""

# нажать на кнопку сохранить
@pytest.fixture()
def create_post_btn_xpath():
    return """//*[@id="create-item"]/div/div/div[7]/div/button"""

# проверить наличие названия поста после сохраннения
@pytest.fixture()
def post_xpath():
    return """//*[@id="app"]/main/div/div[1]/h1"""


