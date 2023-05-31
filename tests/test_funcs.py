import pytest

from utils.funcs import load_operations, executed_operations


@pytest.mark.parametrize('expected', [
    True
])
def test_load_operations(expected):
    assert isinstance(load_operations(), list) == expected


@pytest.mark.parametrize('value, status, expected', [
    (executed_operations(load_operations())[0].values(), 'EXECUTED', True),
    (executed_operations(load_operations())[-15].values(), 'CANCELED', False),
    (executed_operations(load_operations())[-1].values(), 'EXECUTED', True)
])
def test_executed_operations(value, status, expected):
    entrance = status in value
    assert entrance == expected
