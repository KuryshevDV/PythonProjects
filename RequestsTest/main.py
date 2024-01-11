import requests

token = "14f454ea07f4609d4abdc32eca9e6566"

'''response = requests.post('https://api.pokemonbattle.me:9104/trainers/reg', json={
    "trainer_token": token,
    "email": "kuryshev.denis@yandex.ru",
    "password": "1111111"}, 
    headers = {"Content-Type" : "application/json"})
print(response.text)'''




response_create = requests.post('https://api.pokemonbattle.me:9104/pokemons', json={
    "name": "Generate",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"}, 
     headers = {"Content-Type" : "application/json", "trainer_token": token})

print(response_create.text)


response_rename = requests.put('https://api.pokemonbattle.me:9104/pokemons', json={
    "pokemon_id": "26861",
    "name": "Raizen",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"}, 
     headers = {"Content-Type" : "application/json", "trainer_token": token})

print(response_rename.text)


response_catch = requests.post('https://api.pokemonbattle.me:9104/trainers/add_pokeball', json={
    "pokemon_id": "26861"}, 
     headers = {"Content-Type" : "application/json", "trainer_token": token})

print(response_catch.text)