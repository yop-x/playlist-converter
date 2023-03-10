from bs4 import BeautifulSoup
import requests 


# Using beautiful soup to extract the web elements 
# Need to log in

url = 'https://music.163.com/#/playlist?id=2313062981'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')



# Returned some element but the playlist is hidden under 'iframe' 
# Download the 'view frame source' html file to try out 
# Getting the class_ name that contains all the songs ids

song_ids = []

path = './view-source_https___music.163.com_playlist_id=2313062981.html'

with open(path) as fp:
    soup2 = BeautifulSoup(fp, 'html.parser')
    
songs = soup2.find_all(class_='html-attribute-value html-external-link')
for song in songs:
    if '/song?id' in song.text:
        song_ids.append(song.text[9:])
    
print(song_ids)
print(len(song_ids))

api_url = 'https://music.163.com/api/song/detail/?id=26547431&ids=[26547431]' 

new_response = requests.get(api_url)

song_names = []
for id in song_ids:
    api_url = f'https://music.163.com/api/song/detail/?id={id}&ids=[{id}]'
    print(requests.get(api_url).json()['songs'][0]['name'])