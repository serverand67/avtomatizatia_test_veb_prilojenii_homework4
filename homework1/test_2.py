import requests
import yaml
from conftest import auth_token
import pytest

with open(r'C:\Users\NiKa\PycharmProjects\avtomatizatia_test_veb_prilojenii\homework1\config.yaml') as f:
    data = yaml.safe_load(f)



def test_check_post_title(auth_token):
    res_get = requests.get(url=data['url2'], headers={"X-Auth-Token": auth_token}, params={"owner": "notMe"})
    res_json = res_get.json()
    assert res_get.status_code == 200
    assert 'data' in res_json

    post_titles = [post["title"] for post in res_json["data"]]
    assert data["title"] in post_titles

