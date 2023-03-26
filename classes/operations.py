import json

class Operations():

    def __init__(self, data):
        with open(data) as f:
            self.data = json.loads(f.read())

    def __repr__(self):
        return f"Transactions('{self.data}')"

    def counter(self):
        return f"Number of transactions: {len(self.data)}"

    def get_last_ex(self, number):
        sorted_by_date = sorted(self.data, key=lambda transaction: (transaction['state'], transaction['date']), reverse=True)
        return sorted_by_date[:number]

    def get_last_all(self, number):
        sorted_by_date = sorted(self.data, key=lambda transaction: transaction['date'], reverse=True)
        return sorted_by_date[:number]