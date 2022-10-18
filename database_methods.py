import json_data_provider as js
import os.path


# Инициализация
def initialization():
    file = os.path.isfile("data_file.json")
    if file == False:
        data = []
        js.write_in_file(data)
    # чтение существующего файла
    data = js.read_file()
    return data


# Показать Базу Данных
def show(data):
    if not data:
        print('База данных пуста. Заполните БД.')
        return
    for i, item in enumerate(data):
        item_str = str(item).translate({ord(i): None for i in '{' '}' '\''})
        print(f'{i}. {item_str}')


# Добавить новое поле
def get_add_key(data):
    if not data:
        print('База данных пуста. Заполните БД.')
        return
    user = input('Введите название нового поля ')
    for x in data:
        x[user] = '*'
    return data


# Добавить учетную запись
def get_add_user(data):
    if not data:
        user = {}
        user['Фамилия'] = input('Фамилия ')
        user['Имя'] = input('Имя ')
        user['Отчество'] = input('Отчество ')
    else:
        a = data[0]
        user = {}
        for i in a:
            user[i] = input(f'{i} ')

    data.append(user)
    return data


# Поиск пользователя
def get_user_search(data):
    if not data:
        print('База данных пуста. Заполните БД.')
        return
    key_user = input('Введите название столбца ')
    value_user = input('Введите данные поиска ')
    find_all_by_key(data, key_user, value_user)


# Поиск значения по ключу
def find_all_by_key(iterable, key, value):
    is_not_exist = True
    for index, dict_ in enumerate(iterable):
        if key in dict_ and dict_[key] == value:
            item_str = str(dict_).translate(
                {ord(i): None for i in '{' '}' '\''})
            print(f'{index}. {item_str}')
            is_not_exist = False
    if is_not_exist:
        print("Данные не найдены")
