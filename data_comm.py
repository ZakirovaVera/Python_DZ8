import menu
import json_data_provider as js
import database_methods as dm


def data_comm():
    number = -1
    data = dm.initialization()
    while number != 0:
        number = menu.view()
        if number == 1:
            dm.show(data)  # Вывод бд
        if number == 2:
            dm.get_add_key(data)  # Добавить новое поле
        if number == 3:
            dm.get_add_user(data)  # Добавить учетную запись
        if number == 4:
            dm.get_user_search(data)  # Поиск пользователя
        js.write_in_file(data)
        print()

# def data_comm():
#     data = json_data_provider.read_file()
#     exit = True
#     while exit:
#         what = menu.menu()
#         if what == 1:
#             get_выводить_базу()
#         elif what == 2:
#             ak.get_add_key(data)
#         elif what == 3:
#             get_add_user(data)
#         elif what == 4:
#             get_поиск_данные_пользователя()
#         else:
#             json_data_provider.write_in_file(data)
#             exit = False
