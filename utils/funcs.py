import json
import arrow


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
    executed_operations = []

    for item in all_operations:
        if 'EXECUTED' in item.values():
            executed_operations.append(item)

    return executed_operations[-5::]


def get_operation_date(operation_info: dict):
    if 'date' in operation_info.keys():
        convert_date = str(arrow.get(operation_info['date']).date())
        date_list = convert_date.split('-')
        operation_date = '.'.join(date_list[::-1])
    else:
        operation_date = 'Дата не записана'

    return operation_date


def get_card(operation_info: dict):
    if 'to' in operation_info.keys():
        security_card_num_to = '**' + operation_info['to'][-4::]
    else:
        security_card_num_to = 'Нет данных о получателе'
    if 'from' in operation_info.keys():
        security_card_num_from = f"{operation_info['from'][:-12]} {operation_info['from'][-12:-10]}** **** {operation_info['from'][-4::]}"
    else:
        security_card_num_from = 'Нет данных об отправителе'

    return security_card_num_from, security_card_num_to,


def get_operations_details(operation_info: dict):
    return f"""{get_operation_date(operation_info)} {operation_info['description']}
{get_card(operation_info)[0]} -> {get_card(operation_info)[1]}
{operation_info['operationAmount']['amount']} руб.
"""
