import json_data_provider as js
import os.path


# Инициализация
def initialization():
    file = os.path.isfile("data_file.json")
    if file == False:
        data = []
        js.write_in_file(data)

    data = js.read_file()
    return data


# Показать Базу Данных
def show(data):
    for i, item in enumerate(data):
        item_str = str(item).translate({ord(i): None for i in '{' '}' '\''})
        print(f'{i}. {item_str}')

# Добавить новое поле
def get_add_key(data):
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

