def view():
    """
    Меню БЗ
    return: выбранную операцию с БЗ
    """
    point = -1

    text_menu = ("МЕНЮ - База сотрудников\n"
                 "1. Показать Базу Данных\n"
                 "2. Добавить новое поле\n"
                 "3. Добавить учетную запись\n"
                 "4. Поиск пользователя\n"
                 "0. Выход"
                 )
    print(text_menu)
    print()

    while True:
        try:
            point = int(input("Введите номер пункта меню: "))
            if point in [1, 2, 3, 4, 0]:
                break
        except ValueError:
            print("Введён неправильный пункт меню. Попробуйте ещё раз.")
    return point
