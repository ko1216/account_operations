import json
import arrow
import os


def load_operations():
    """
    Функция строит универсальный путь до файла, после этого открывает его и рапаковывает из json
    :return: list
    """
    operations_path = os.path.join(os.path.dirname('D:/Any_Python_Projects/account_operations/'), 'operations.json')

    with open(operations_path, 'r', encoding='utf-8-sig') as f:
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
    """
    Функция возвращает дату в формате "дд.мм.гггг", если она была записана в массиве
    :param operation_info: dict
    :return: str
    """
    if 'date' in operation_info.keys():
        convert_date = str(arrow.get(operation_info['date']).date())
        date_list = convert_date.split('-')
        operation_date = '.'.join(date_list[::-1])
    else:
        operation_date = 'Дата не записана'

    return operation_date


def get_card(operation_info: dict):
    """
    Функция возвращает в зашифрованном виде, если информация есть в массиве:
    Платежную систему карты отправителя и ее номер в формате 0000 00** **** 0000
    Последние 4 цифры карты полчателя в формате **0000
    :param operation_info: dict
    :return: str
    """
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
    """
    Функция возвращает строку содержащую в себе инфо об операции в формате:
    "дата перевода, род операции
    карта отправителя -> карта получателя
    сумма в рублях"
    :param operation_info: dict
    :return: str
    """
    return f"""{get_operation_date(operation_info)} {operation_info['description']}
{get_card(operation_info)[0]} -> {get_card(operation_info)[1]}
{operation_info['operationAmount']['amount']} руб.
"""
