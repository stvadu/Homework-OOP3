import requests

url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
names_of_characters = ['Hulk','Captain America','Thanos']
intelligence_dict = {}
def hero_request():
    response = requests.get(url)
    characters_list = response.json()
    for hero in characters_list:
        intelligence = hero['powerstats']['intelligence']
        if hero['name'] in names_of_characters:
            intelligence_dict[hero['name']] = intelligence
    sorted_intelligence_dict = sorted([(value, key)
                                       for (key, value) in intelligence_dict.items()])
    print(f' Самый умный герой - {sorted_intelligence_dict[-1][1]} co значением intelligence {sorted_intelligence_dict[-1][0]}')

if __name__ == '__main__':
    hero_request()