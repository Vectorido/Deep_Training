import requests, json

client_id = '934ff4a6da0986a2e6b8'  # используем полученные после регистрации идентификаторы
client_secret = '153768a3dfc3cfaad7820d850ec2d60e'

r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      'client_id': client_id,
                      'client_secret': client_secret
                  })  # инициируем запрос на получение токена
j = json.loads(r.text)
token = j["token"]

with open('C:/Users/Hurricane/Downloads/dataset_24476_4.txt', 'r', encoding='UTF-8') as file:
    data = file.read().strip().split('\n')  # считываем данные об артистах из файла

headers = {"X-Xapp-Token": token}  # создаем заголовок, содержащий наш токен

artists = {}  # создаем словарь и передаём запросы поэлементно из считанного файла
for i in data:
    r = requests.get(f"https://api.artsy.net/api/artists/{i}", headers=headers)
    artist, birthday = r.json()['sortable_name'], r.json()['birthday']
    artists[artist] = birthday

sorted_artists = sorted(artists.items(), key=lambda x: (x[1], x[0]))  # создаем отсортированный список
print(sorted_artists)
print(*[i[0] for i in sorted_artists], sep='\n')
