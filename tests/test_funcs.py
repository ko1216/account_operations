import pytest

from utils.funcs import load_operations, get_latest_executed_operations, get_operation_date, mask_account_number, \
    data_sorted_operations


@pytest.mark.parametrize('expected', [
    True
])
def test_load_operations(expected):
    assert isinstance(load_operations(), list) == expected


@pytest.mark.parametrize('value, status, expected', [
    (get_latest_executed_operations(load_operations())[0].values(), 'EXECUTED', True),
    (get_latest_executed_operations(load_operations())[-1].values(), 'CANCELED', False),
    (get_latest_executed_operations(load_operations())[3].values(), 'EXECUTED', True)
])
def test_get_latest_executed_operations1(value, status, expected):
    entrance = status in value
    assert entrance == expected


def test_get_latest_executed_operations2():
    assert len(get_latest_executed_operations(load_operations())) == 5


@pytest.mark.parametrize('operation_info, expected', [
    ({'date': '2018-12-24'}, '24.12.2018'),
])
def test_get_operation_date(operation_info, expected):
    assert get_operation_date(operation_info) == expected


@pytest.mark.parametrize('operation_info, expected0, expected1', [
    ({'to': '0000111122223333', 'from': 'какой бы не был длинный текст Платежной системы 0000111122223333'},
     'какой бы не был длинный текст Платежной системы 0000 11** **** 3333', '**3333'),
    ({'from': 'какой бы не был длинный текст Платежной системы 0000111122223333'},
     'какой бы не был длинный текст Платежной системы 0000 11** **** 3333', 'Нет данных о получателе'),
    ({'to': '0000111122223333'}, 'Нет данных об отправителе', '**3333'),
    ({'from': 'счет 00001111222233334444'},
     'счет 0000************4444', 'Нет данных о получателе')
])
def test_mask_account_number(operation_info, expected0, expected1):
    assert mask_account_number(operation_info) == (expected0, expected1)


@pytest.mark.parametrize('operations, expected', [
    ([{'date': '2018-06-24T00:46:32.422648'}, {'date': '2019-09-06T00:48:01.081967'}], True),
    ([{'date': '2019-10-15'}, {'date': '2018-01-20'}], True)
])
def test_data_sorted_operations(operations, expected):
    test_expected = data_sorted_operations(operations)[0]['date'] < data_sorted_operations(operations)[-1]['date']
    assert test_expected == expected
