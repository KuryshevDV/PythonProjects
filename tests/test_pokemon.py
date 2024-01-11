import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'
token = "14f454ea07f4609d4abdc32eca9e6566"

def test_status_code():
    response = requests.get(f'{host}/trainers', params={'trainer_id' : 3474})
    assert response.status_code == 200
    
def test_name_trainer():
        response = requests.put(f'{host}/trainers', headers = {"trainer_token" : token},
        json={
        "name": "Den",
        "city": "Самара"
        })
        assert response.json()["message"] == "Информация о тренере обновлена"