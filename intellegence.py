import requests

hero_list = ['Hulk', 'Captain America', 'Thanos']
hero_int = {}
for heroes in hero_list:
  url = 'https://superheroapi.com/api/2619421814940190/search/'+ heroes
  response = (requests.get(url))
  a = response.json()
  for char in a['results']:
    if char['name'] in hero_list:
      hero_int[char['name']] = char['powerstats']['intelligence']
print(max(hero_int))