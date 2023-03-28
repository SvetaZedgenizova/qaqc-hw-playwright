import requests
import pytest
from config import url_pokemon


def get_pokemon(id, name):
    url = f'{url_pokemon}{id}'
    req = requests.get(url=url)
    assert req.status_code == 200
    r = req.json()
    assert r['name'] == name
    return r['awesome_names'][0]['awesome_name']


def test_get_pokemons():
    pokemon1 = get_pokemon(1, 'ball')
    print(pokemon1)

    pokemon2 = get_pokemon(2, 'squiggle')
    print(pokemon2)

    pokemon3 = get_pokemon(3, 'fish')
    print(pokemon3)

    pokemon4 = get_pokemon(4, 'arms')
    print(pokemon4)

    pokemon5 = get_pokemon(5, 'blob')
    print(pokemon5)





