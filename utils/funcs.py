import json


def load_operations():
    with open('../operations.json', 'r', encoding='utf-8-sig') as f:
        """
        Функция из файла json.txt распаковывает и возвращает список операций
        """
        operations = json.load(f)
        return operations



