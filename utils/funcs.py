import json


def load_operations():
    with open('../operations.json', 'r', encoding='utf-8-sig') as f:
        """
        Функция из файла json.txt распаковывает и возвращает список операций
        """
        operations = json.load(f)
        return operations


def executed_operations(data):
    executed_operation = []

    for item in data:
        if 'EXECUTED' in item.values():
            executed_operation.append(item)

    return executed_operation

