from datetime import datetime


def hide_group_card_data(data):
    """
    Функция скрывает часть номера карты или счета символами **** и группирует номер карты по 4-е цифры
    Если данные о карте/счете отсутствуют, то возвращается сообщение строковое значение "Наличные"
    :param data: Списковый словарь одной операции пользователя
    :return: строка с обработанным номером карты/счета или "Наличные"
    """

    # Проверяем есть ли в словаре информация об источнике платежа.
    if 'from' in data:
        # Проверяем источник платежа: счет или карта
        if 'Счет' in data['from']:
            # Возвращаем отфоматированный номер счета
            return 'Счет **' + data['from'][-4:]

        else:
            # Разделяем тип карты и номер
            card_number = data['from'][-16:]
            card_type = data['from'][:-17]
            # Скрываем часть номера карты
            card_number_hidden = card_number[0:6] + '******' + card_number[-4:]
            card_number_grouped = []

            # Разделяем номер карты по 4 цифры
            for i in range(0, 13, 4):
                card_number_grouped.append(card_number_hidden[i:i + 4])

            # Возвращаем отформатированный номер карты
            return f'{card_type} {" ".join(card_number_grouped)}'

    else:
        # Возвращаем инфо, что платеж был наличными
        return f'Наличные'


def hide_account(data):
    """
    Функция скрывает часть номера cчёта, который сделан перевод символами ****
    :param data: Списковый словарь одной операции пользователя
    :return: строка с обработанным счета
    """

    return 'Счет **' + data['to'][-4:]


def format_date(data):
    """
    Функция преобразует и возвращает дату в формате "%d.%m.%Y"
    :param data: Списковый словарь одной операции пользователя
    :return: строка с датой
    """

    # Находим значение даты
    date = data['date']
    # Создаем датафрайм
    date_frame = datetime.strptime(date[:10], '%Y-%m-%d')
    # Форматируем дату в необходимом формате
    formatted_date = date_frame.strftime("%d.%m.%Y")

    return formatted_date


def get_amount(data):
    """
    Функция возвращает сумму операции в формате: <Сумма> <валюта>
    :param data: Списковый словарь одной операции пользователя
    :return: строка с отформатированной суммой
    """

    return f"{data['operationAmount']['amount']} {data['operationAmount']['currency']['name']}"


def get_operation_details(data):
    """
    Функция возвращает информацию об операциях пользоваталея в формате:
    <дата перевода> <описание перевода>
    <откуда> -> <куда>
    <сумма перевода> <валюта>
    :param data: Списковый словарь с операциями пользователя
    :return: построковый вывод информации в необходимом формате
    """

    # Выводим информацию для каждой операции в словаре
    for item in data:
        print(f"{format_date(item)} {item['description']}\n{hide_group_card_data(item)} --> {hide_account(item)}"
              f"\n{get_amount(item)}\n\n")
