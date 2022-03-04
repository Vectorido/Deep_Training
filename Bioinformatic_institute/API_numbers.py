import requests, json

with open('C:/Users/Hurricane/Downloads/dataset_24476_3.txt', 'r', encoding='UTF-8') as file:
    data = file.read().strip().split('\n')
    print(data)
    req_data = ', '.join(data)
    print(req_data)

for i in data:
    api_url = f'http://numbersapi.com/{i}/math?json=true'
    res = requests.get(api_url)
    # print(res.status_code)
    json_data = res.json()
    if json_data['found']:
        print('Interesting')
    else:
        print('Boring')

params = {
    'number': 4,
    'type': 'math',
}

# res = requests.get(api_url)
#
# print(res.status_code)
# print(res.json())
