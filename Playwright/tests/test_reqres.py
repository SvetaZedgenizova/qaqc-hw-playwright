import requests
import pytest
from config import *

def test_get_list():
    req = requests.get(url_get_list)
    assert req.status_code == 200 
    r = req.json()
    assert (r['data'][0]['first_name']) == first_name
    print(r['data'][0]['first_name'])
    return r



def test_create_user():
    req = requests.post(url=url_create_user, data=params_create_user)
    assert req.status_code == 201
    r = req.json()
    assert (r['name']) == name
    print(r['name'])
    return r


def test_update_user():
    req = requests.put(url=url_update_user,data=params_update_user)
    assert req.status_code == 200
    r = req.json()
    print(r['name'])
    assert (r['name']) == name_update

test_create_user()
test_get_list()
test_update_user()