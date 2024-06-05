import pytest
from datetime import datetime
from src.func import get_json, my_data, last_5, mask

def test_get_json():
    with pytest.raises(FileNotFoundError):
        get_json('fsfa')

def test_my_data():
    assert my_data([]) == []
    assert my_data([{}, {'one': 'two'}]) == []
    assert my_data([{'date': "2019-08-26T10:50:58.294041", 'state': "EXECUTED"}]) == [{'date': datetime.fromisoformat("2019-08-26T10:50:58.294041"), 'state': "EXECUTED"}]

def test_last_5():
    assert last_5([]) == []
    assert last_5([
        {'date': 2},
        {'date': 3},
        {'date': -5},
        {'date': 11},
        {'date': 0},
        {'date': 4}
    ]) == [{'date': 11}, {'date': 4}, {'date': 3}, {'date': 2}, {'date': 0}]

def test_mask():
    assert mask("Счет 64686473678894779589") == 'Счет **9589'
    assert mask("Visa Classic 6831982476737658") == 'Visa Classic 6831 98** **** 7658'