import pytest
import requests

from url import *
from data import *


@pytest.fixture
def create_new_user_and_delete():
    payload_cred = {
        'email': create_random_email(),
        'password': create_random_password(),
        'name': create_random_username()
    }
    response = requests.post(Urls.USER_REGISTER, data=payload_cred)
    response_body = response.json()

    yield payload_cred, response_body

    access_token = response_body['accessToken']
    requests.delete(Urls.USER_DELETE, headers ={'Authorization': access_token})


@pytest.fixture
def create_user_and_order_and_delete(create_new_user_and_delete):
    access_token = create_new_user_and_delete[1]['accessToken']
    headers = {'Authorization': access_token}
    payload = {'ingredients': [Burger.CORRECT_HASH]}
    response_body = requests.post(Urls.URL_ORDER, data=payload, headers=headers)

    yield access_token, response_body

    requests.delete(Urls.USER_DELETE, headers={'Authorization': access_token})