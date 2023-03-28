from utils.widget_output import hide_group_card_data, format_date, get_amount, hide_account


data_1 = {'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582',
          'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}},
          'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'}

data_2 = {'id': 482520625, 'state': 'EXECUTED', 'date': '2019-11-13T17:38:04.800051',
          'operationAmount': {'amount': '62814.53', 'currency': {'name': 'руб.', 'code': 'RUB'}},
          'description': 'Перевод со счета на счет', 'from': 'Счет 38611439522855669794',
          'to': 'Счет 46765464282437878125'}

data_3 = {'id': 154927927, 'state': 'EXECUTED', 'date': '2019-11-19T09:22:25.899614',
          'operationAmount': {'amount': '30153.72', 'currency': {'name': 'руб.', 'code': 'RUB'}},
          'description': 'Перевод организации', 'from': 'Maestro 7810846596785568',
          'to': 'Счет 43241152692663622869'}


def test_hide_group_card_data():
    assert hide_group_card_data(data_1) == 'Наличные'
    assert hide_group_card_data(data_2) == 'Счет **9794'
    assert hide_group_card_data(data_3) == 'Maestro 7810 84** **** 5568'


def test_format_date():
    assert format_date(data_1) == '08.12.2019'


def test_get_amount():
    assert get_amount(data_2) == '62814.53 руб.'

def test_hide_account():
    assert hide_account(data_3) == 'Счет **2869'
