# Создание набора для пользователя:

Был создан набор внутри конкретного пользователя.

Для этого предварительно мы сделали:

1. выполнили запрос на создание нового пользователя, запомнили токен авторизации authToken.
2. выполнили запрос на создание личного набора для этого пользователя, передали заголовок Authorization.
3. дальше использовали чек-лист.

# Проведенные тесты:

__Тест 1. Успешное создание набора. Параметр Name состоит из 1 символа__
def test_create_kit_1_letter_in_name_get_success_response()

__Тест 2. Успешное создание набора. Параметр Name состоит из 511 символов__
def test_create_kit_511_letters_in_name_get_success_response()

__Тест 3. Ошибка. Параметр Name состоит из 0 символов__
def test_create_kit_empty_name_get_success_response()

__Тест 4. Ошибка. Параметр Name состоит из 512 символов__
def test_create_kit_512_letters_in_name_get_success_response()

__Тест 5. Успешное создание набора. Параметр Name состоит из английских букв__
def test_create_kit_english_letters_in_name_get_success_response()

__Тест 6. Успешное создание набора. Параметр Name состоит из русских букв__
def test_create_kit_russian_letters_in_name_get_success_response()

__Тест 7. Успешное создание набора. Параметр Name состоит из спецсимволов__
def test_create_kit_has_special_symbols_in_name_get_success_response()

__Тест 8. Успешное создание набора. Параметр Name состоит из слов с пробелами__
def test_create_kit_has_spaces_in_name_get_success_response()

__Тест 9. Успешное создание набора. Параметр Name состоит из цифр__
def test_create_kit_has_numbers_in_name_get_success_response()

__Тест 10. Ошибка. В запросе нет параметра Name__
def test_create_kit_no_name_get_error_response()

__Тест 11. Ошибка. Тип параметра Name: число__
def test_create_kit_intejer_in_name_get_success_response()