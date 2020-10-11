#comment


with open('data.txt') as json_file:
    datas = json.load(json_file)
    for p in datas['products']:
        print('Name: ' + p['name'])
        print('Price: $' + p['price'])
        print('')