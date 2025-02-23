import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '766a80310b30390ece7d45916a654931'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "generate",
    "photo_id": -1
}

body_change = {
    "pokemon_id": "242829",
    "name": "kisskissskiss",
    "photo_id": -1
}

body_add_pokeball = {
    "pokemon_id": "224187"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

pokemon_id = response_create.json()['id']
print(pokemon_id)'''

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)

message = response_change.json()['message']
print(message)

'''response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)

message = response_add_pokeball.json()['message']
print(message)'''

