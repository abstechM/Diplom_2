import pytest
import allure
import requests

from url import *
from data import *


class TestRegistration:
    @allure.title('Тест успешной регистрации')
    def test_reg_success(self):
        payload = {
            'email': create_random_email(),
            'password': create_random_password(),
            'name': create_random_username()
        }
        response = requests.post(Urls.USER_REGISTER, data=payload)
        assert response.status_code == 200
        assert response.json()['success'] is True
        assert response.json()['user']['email'] == payload['email']
        assert response.json()['user']['name'] == payload['name']

        # удаление данных после теста
        access_token = response.json()['accessToken']
        requests.delete(Urls.USER_DELETE, headers={'Authorization': access_token})


    @allure.title('Тест обязательных полей при регистрации')
    @pytest.mark.parametrize('field', [EmptyField.EMPTY_NAME, EmptyField.EMPTY_EMAIL, EmptyField.EMPTY_PSWD])
    def test_reg_empty_failed(self, field):
        response = requests.post(Urls.USER_REGISTER, data=field)
        assert response.status_code == 403
        assert response.json() == ReqText.ERROR_EMPTY_FIELD

    @allure.title('Тест регитсрации с имеющимся email в базе')
    def test_reg_same_email(self):
        payload = {
            'email': UserData.EMAIL,
            'password': create_random_password(),
            'name': create_random_username()
        }
        response = requests.post(Urls.USER_REGISTER, data=payload)
        assert response.status_code == 403
        assert response.json() == ReqText.REPEAT_REG