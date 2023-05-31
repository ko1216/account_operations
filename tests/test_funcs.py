import pytest

from utils.funcs import load_operations


def test_load_operations():
    assert load_operations() == list
