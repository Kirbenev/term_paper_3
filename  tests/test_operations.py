from classes.operations import Operations

def test_counter():
    test = Operations('test_data')
    assert test.counter() == 'Number of transactions: 3'

def test_get_last_ex():
    test = Operations('test_data')
    assert test.get_last_ex(1) == [{'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582',
          'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}},
          'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'}]

def test_get_last_all():
    test = Operations('test_data')
    assert test.get_last_all(1) == [{'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582',
          'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}},
          'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'}]