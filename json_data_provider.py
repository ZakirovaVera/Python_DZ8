import json


def read_file():
    with open("data_file.json", "r", encoding='utf8') as read_file:
        string = read_file.read()
        data = json.loads(string)
    return data


def write_in_file(data):
    with open("data_file.json", "w", encoding='utf8') as write_file:
        json.dump(data, write_file, ensure_ascii=False, indent=4)
