import configuration
import requests
import data

# данная функция отправялет запрос на создание нового пользователя
def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=user_body, headers=data.headers)

# данная  функция возвращает токен авторизации из  функции  выше - def post_new_user(user_body):
def get_new_user_token():
    response = post_new_user(data.user_body)
    return response.json()['authToken']

# данная функция делает запрос на создание набора, используя словарь kit_body и токен авторизации
def post_new_client_kit(kit_body, auth_token):
    headers_dict = data.headers.copy()
    headers_dict["Authorization"] = "Bearer " + auth_token
    url = configuration.URL_SERVICE + configuration.CREATE_KIT_PATH
    response = requests.post(url, json=kit_body, headers=headers_dict)
    return response
    # return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITH_PATH, json=kit_body, headers=headers_dict)
