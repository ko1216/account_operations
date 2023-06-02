import pytest

from utils.funcs import load_operations, get_latest_executed_operations


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
