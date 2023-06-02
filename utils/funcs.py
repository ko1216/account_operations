import json


def load_operations():
    with open('D:/Any_Python_Projects/account_operations/operations.json', 'r', encoding='utf-8-sig') as f:
        """
        Функция из файла json распаковывает и возвращает список операций
        """
        operations = json.load(f)
        return operations


def get_latest_executed_operations(all_operations):
    """
    Функция возвращает список операций со статусом EXECUTED
    :param all_operations: list
    :return: list
    """
    executed_operation = []

    for item in all_operations:
        if 'EXECUTED' in item.values():
            executed_operation.append(item)

    return executed_operation[-5::]

