import sender_stand_request
import data


#  Вызываем функцию post_new_user в файле sender_stand_request.py и извлекаем из ответа сервера
#  токен нового пользователя, используюя ключ 'authToken'.
response = sender_stand_request.post_new_user(data.user_body)
auth_token = response.json()['authToken']


# Функция для изменения значения в параметре Name в теле запроса
def get_kit_body(name):
# Копируется словарь с телом запроса из файла data
    current_body = data.kit_body.copy()
# Изменение значения в поле Name
    current_body["name"] = name
# Возвращается новый словарь с нужным значением Name
    return current_body


# Функция для позитивной проверки
def positive_assert(name):
# В переменную kit_body сохраняется обновлённое тело запроса
    kit_body = get_kit_body(name)
# В переменную kit_response сохраняется результат запроса на создание набора и токен аутентификации auth_token
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
#  Проверяем, что код ответа равен 201
    assert kit_response.status_code == 201
#  Проверяем, что поле name в ответе совпадает с полем name в запросе
    assert kit_response.json()["name"] == name


# Функция негативной проверки, когда в ответе ошибка про символы
def negative_assert_symbol(name):
# В переменную kit_body сохраняется обновлённое тело запроса
    kit_body = get_kit_body(name)
# В переменную kit_response сохраняется результат создания нового набора и и токен аутентификации auth_token
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
#  Проверяем, что код ответа равен 400
    assert kit_response.status_code == 400
    assert kit_response.json()["name"] != name

# Тест 1. Успешное создание набора. Параметр Name состоит из 1 символа
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")


# Тест 2. Успешное создание набора. Параметр Name состоит из 511 символов
def test_create_kit_511_letters_in_name_get_success_response():
    positive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
abcdabcdabcdabcdabcdabcdabcdabcdabcdabAbcdabcdabcdabcdabcdabcda\
bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabAbcdabcd\
abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
dabcdabAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
cdabcdabcdabcdabcdabAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
abcdabcdabcdabcdabcdabcdabcdabAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
abcdabcdabcdabcdabcdabcdabcdabcdabcdabAbcdabcdabcdabcdabc")


# Тест 3. Ошибка. Параметр Name состоит из 0 символов
def test_create_kit_empty_name_get_success_response():
    negative_assert_symbol("")


# Тест 4. Ошибка. Параметр Name состоит из 512 символов
def test_create_kit_512_letters_in_name_get_success_response():
    negative_assert_symbol("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
abcdabcdabcdabcdabcdabcdabcdabcdabcdabAbcdabcdabcdabcdabcdabcda\
bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabAbcdabcd\
abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
dabcdabAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
cdabcdabcdabcdabcdabAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
abcdabcdabcdabcdabcdabcdabcdabAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
abcdabcdabcdabcdabcdabcdabcdabcdabcdabAbcdabcdabcdabcdabcd")


# Тест 5. Успешное создание набора. Параметр Name состоит из английских букв
def test_create_kit_english_letters_in_name_get_success_response():
    positive_assert("QWErty")


# Тест 6. Успешное создание набора. Параметр Name состоит из русских букв
def test_create_kit_russian_letters_in_name_get_success_response():
    positive_assert("Мария")


# Тест 7. Успешное создание набора. Параметр Name состоит из спецсимволов
def test_create_kit_has_special_symbols_in_name_get_success_response():
    positive_assert("\"№%@\",")


# Тест 8. Успешное создание набора. Параметр Name состоит из слов с пробелами
def test_create_kit_has_spaces_in_name_get_success_response():
    positive_assert(" Человек и КО ")


# Тест 9. Успешное создание набора. Параметр Name состоит из цифр
def test_create_kit_has_numbers_in_name_get_success_response():
    positive_assert("123")


# Тест 10. Ошибка. В запросе нет параметра Name
def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
# удаляем ключ name
    kit_body.pop("name")
# звапрос на создание нового набора с использованием созданного тела и токена аутентификации
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
# проверка, что при отсутствии параметра происходит ошибка 400
    assert kit_response.status_code == 400


# Тест 11. Ошибка. Тип параметра Name: число
def test_create_kit_intejer_in_name_get_success_response():
    negative_assert_symbol(123)