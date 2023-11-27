# Написать тест с использованием pytest и requests, в котором:
#
# Адрес сайта, имя пользователя и пароль хранятся в config.yaml
#
# conftest.py содержит фикстуру авторизации по адресу https://test-stand.gb.ru/gateway/login с передачей параметров “username" и "password" и возвращающей токен авторизации
#
# Тест с использованием DDT проверяет наличие поста
# с определенным заголовком в списке постов другого пользователя, для этого выполняется get запрос по адресу https://test-stand.gb.ru/api/posts c хедером, содержащим токен авторизации в параметре "X-Auth-Token". Для отображения постов другого пользователя передается "owner": "notMe".
#
# http://restapi.adequateshop.com/api/authaccount/registration
#
# http://restapi.adequateshop.com/api/authaccount/login
#
# https://test-stand.gb.ru/login
# https://docs.google.com/spreadsheets/d/1CNSSi72qRuGeWE3WXb8Oi6MHoLqNEuWDC_mZTNiSSHw/edit#gid=165630242
# логин и пароль kitty89  /  61d96a3985

# {'data': [{'id': 88640, 'title': 'Steven', 'description': 'Description', 'content': 'Content', 'authorId': 14698, 'mainImage': {'id': None, 'cdnUrl': ''}, 'updatedAt': '2023-11-22T23:54:10+00:00', 'createdAt': '2023-11-22T23:54:10+00:00', 'labels': [], 'delayPublishTo': None, 'draft': False}


import requests
import yaml

with open(r'C:\Users\NiKa\PycharmProjects\avtomatizatia_test_veb_prilojenii\homework1\config.yaml') as f:
    data = yaml.safe_load(f)

# url1 = "https://test-stand.gb.ru/gateway/login"
# login = "kitty89"
# password = "61d96a3985"
# url2 = "https://test-stand.gb.ru/api/posts"

# result = requests.post(url=url1, data={"username": login, "password": password})
# token = result.json()["token"]
# res_get = requests.get(url=url2, headers={"X-Auth-Token": token}, params={"owner": "notMe"})


result = requests.post(url=data['url1'], data={"username": data['username'], "password": data['password']})
token = result.json()["token"]

res_get = requests.get(url=data['url2'], headers={"X-Auth-Token": token}, params={"owner": "notMe"})

print(res_get)
print(res_get.json())