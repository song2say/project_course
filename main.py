from src.func import get_json, my_data, last_5, mask

def main():
    data = get_json()
    correct = my_data(data)
    operations = last_5(correct)
    for i in operations:
        print(f"{i['date'].strftime('%d.%m.%Y')} {i['description']}")
        print(mask(i.get('from')), '->', mask(i['to']))
        print(i["operationAmount"]["amount"], i["operationAmount"]["currency"]["name"])
        print()

main()