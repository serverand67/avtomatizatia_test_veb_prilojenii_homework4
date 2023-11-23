import requests
import yaml
from conftest import auth_token
import pytest
from ddt import ddt, data

with open(r'C:\Users\NiKa\PycharmProjects\avtomatizatia_test_veb_prilojenii\homework1\config.yaml') as f:
    data = yaml.safe_load(f)

@ddt
def test_check_post_title(auth_token):
    res_get = requests.get(url=data['url2'], headers={"X-Auth-Token": auth_token}, params={"owner": "notMe"})
    assert res_get.status_code == 200, f"Статус код: {res_get.status_code}"
    posts = res_get.json()
    title = data['title']
    post_with_title = any(post.get("title") == title for post in posts)
    assert post_with_title, f"Пост с заголовком '{title}' не найден в списке."

