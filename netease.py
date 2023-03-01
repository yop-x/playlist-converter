import requests 
from bs4 import BeautifulSoup
from NetEaseMusicApi import api
from urllib.parse import urlparse, parse_qs



url = './saved_resource.html'

with open("./saved_resource.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

titles = soup.find_all('span', {'class': 'txt'})

title_list = []
for title in titles:
    title_list.append(title.text)

ids = []
for title in titles:
    url = title.find('a').get('href')
    parsed_url = urlparse(url)
    query_string = parsed_url.query
    query_params = parse_qs(query_string)
    id_value = query_params['id'][0]
    ids.append(id_value)

url  = 'https://music.163.com/api/song/detail/?id=26547431&ids=[26547431]'
response = requests.get(url)
song_data = response.json()
print(song_data)


# for id in ids:
#     api_url = f"https://music.163.com/api/song/detail/?id={id}&ids=[{id}]"
#     response = requests.get(api_url)
#     song_data = response.json()['songs'][0]
#     song_name = song_data['name']
#     print(song_name)
