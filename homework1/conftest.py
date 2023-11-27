import pytest
import requests
import yaml


@pytest.fixture
def auth_token():
    with open(r'C:\Users\NiKa\PycharmProjects\avtomatizatia_test_veb_prilojenii\homework1\config.yaml') as f:
        data = yaml.safe_load(f)

    result = requests.post(url=data['url1'], data={"username": data['username'], "password": data['password']})
    return result.json()["token"]

