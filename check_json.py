import json


def load_data_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Пример использования
data = load_data_from_json('test.json')