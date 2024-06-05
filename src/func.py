import json
from datetime import datetime

def get_json(path='main/operations.json'):
    with open(path, encoding='utf-8') as file:
        data = json.load(file)
    return data

def my_data(data):
    my_list = []
    for i in data:
        if i and i.get('date') is not None and i['state'] == 'EXECUTED':
            i['date'] = datetime.fromisoformat(i['date'])
            my_list.append(i)
    return my_list

def last_5(data):
    data = sorted(data, key=lambda x: x['date'], reverse=True)[:5]
    return data

def mask(one):
    if one is None:
        return ''
    sup = one.split()
    if sup[0] == 'Счет':
        return f'Счет **{sup[-1][-4:]}'
    else:
        my_list = sup[-1]
        my_list = my_list[:6] + ('*' * 6) + my_list[-4:]
        my_list = my_list[:4] + ' ' + my_list[4:8] + ' ' + my_list[8:12] + ' ' + my_list[12:]
        return ' '.join(sup[:-1]) + ' ' + my_list