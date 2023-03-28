import json


class Operations:
    """
    Класс "Операции"
    **Поля:**
      -Список с вложенными словаря с данными об операциях
    **Методы:**
       -подсчет количества операций (вернет int)
       -вывод заданного количества последних выполненных операций
       -вывод заданного количества последних всех операций
    При инициализации отрывается файл-источник с данными об операциях и преобразуется в списочный словарь
    """

    def __init__(self, data):
        with open(data) as f:
            self.data = json.loads(f.read())

    def __repr__(self):
        return f"Transactions('{self.data}')"

    def counter(self):
        """
        Возвращает количество операций
        """
        return f"Number of transactions: {len(self.data)}"

    def get_last_ex(self, number):
        """
        Возвращает number последних выполненных операций
        :param number: int, количество операций которые необходимо вывести
        :return: списковый словарь
        """

        sorted_by_date = sorted(self.data,
                                key=lambda transaction: (transaction['state'], transaction['date']),
                                reverse=True)

        return sorted_by_date[:number]

    def get_last_all(self, number):
        """
        Возвращает number последних всех операций
        :param number: int, количество операций которые необходимо вывести
        :return: списковый словарь
        """

        sorted_by_date = sorted(self.data, key=lambda transaction: transaction['date'], reverse=True)
        return sorted_by_date[:number]
