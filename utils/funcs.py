import json
import arrow
import os


def load_operations():
    """
    Функция строит универсальный путь до файла, после этого открывает его и рапаковывает из json
    :return: list
    """
    operations_path = os.path.join(os.path.dirname(__file__), 'operations.json')

    with open(operations_path, 'r', encoding='utf-8-sig') as f:
        operations = json.load(f)
        return operations


def data_sorted_operations(all_operations: list):
    """
    Функция сортирует весь список операций по дате, если она указана.
    Возвращает список операций отсортированный по дате.
    :param all_operations: list
    :return: list
    """
    date_in_list = []

    for item in all_operations:
        if 'date' in item.keys():
            item['date'] = str(arrow.get(item['date']).date())
            date_in_list.append(item)

    date_in_list.sort(key=lambda x: x['date'])
    return date_in_list


def get_latest_executed_operations(sorted_operations: list):
    """
    Функция возвращает список из 5 последних операций со статусом EXECUTED
    :param sorted_operations: list
    :return: list
    """
    executed_operations = []

    for item in sorted_operations:
        if 'EXECUTED' in item.values():
            executed_operations.append(item)

    return executed_operations[-5::]


def get_operation_date(operation_info: dict):
    """
    Функция возвращает дату, удобную для чтения, в формате "дд.мм.гггг"
    :param operation_info: dict
    :return: str
    """
    date_list = operation_info['date'].split('-')
    operation_date = '.'.join(date_list[::-1])

    return operation_date


def mask_account_number(operation_info: dict):
    """
    Функция возвращает в зашифрованном виде, если информация есть в массиве:
    Платежную систему карты отправителя и ее номер в формате 0000 00** **** 0000
    Последние 4 цифры карты полчателя в формате **0000
    :param operation_info: dict
    :return: str
    """
    if 'to' in operation_info.keys():
        mask_num_to = '**' + operation_info['to'][-4::]
    else:
        mask_num_to = 'Нет данных о получателе'
    if 'from' in operation_info.keys():
        if 'счет' in operation_info['from'].lower():
            mask_num_from = f"{operation_info['from'][:-16]}{'*' * 12}{operation_info['from'][-4::]}"
        else:
            mask_num_from = f"{operation_info['from'][:-12]} {operation_info['from'][-12:-10]}** **** {operation_info['from'][-4::]}"
    else:
        mask_num_from = 'Нет данных об отправителе'

    return mask_num_from, mask_num_to


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
{mask_account_number(operation_info)[0]} -> {mask_account_number(operation_info)[1]}
{operation_info['operationAmount']['amount']} руб.
"""
