from datetime import datetime


def hide_group_card_data(data):
    if 'from' in data:
        if 'Счет' in data['from']:
            return ('Счет **' + data['from'][-4:])

        else:

            card_number = data['from'][-16:]
            card_type = data['from'][:-17]
            card_number_hidden = card_number[0:6] + '******' + card_number[-4:]
            card_number_grouped = []

            for i in range(0, 13, 4):
                card_number_grouped.append(card_number_hidden[i:i + 4])

            return f'{card_type} {" ".join(card_number_grouped)}'

    else:
        return f'Наличные'

def hide_account(data):
    return ('Счет **' + data['to'][-4:])

def format_date(data):

    date = data['date']
    date_frame = datetime.strptime(date[:10], '%Y-%m-%d')
    formatted_date = date_frame.strftime("%d.%m.%Y")

    return formatted_date

def get_amount(data):
    return f"{data['operationAmount']['amount']} {data['operationAmount']['currency']['name']}"

def get_operation_details(data):

    for item in data:

        print(f"{format_date(item)} {item['description']}\n{hide_group_card_data(item)} --> {hide_account(item)}\n{get_amount(item)}\n\n")


