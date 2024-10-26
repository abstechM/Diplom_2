import requests

from conftest import *
import allure


class TestUserUpdate:

    @allure.title('Проверка ответа на запрос изменения данных аутентифицированного пользователя')
    def test_update_user_auth(self, create_new_user_and_delete):
        data = {
            'email': create_random_email(),
            'password': create_random_password(),
            'name': create_random_username()
        }
        response = requests.patch(Urls.USER_UPDATE, headers={
            'Authorization': create_new_user_and_delete[1]['accessToken']}, data = data)
        assert response.status_code == 200
        assert response.json()['success'] is True
        assert response.json()['user']['email'] == data['email']
        assert response.json()['user']['name'] == data['name']

    @allure.title('Проверка ответа на запрос изменения данных неаутентифицированного пользователя')
    def test_update_user_whitout_auth(self):
        data = {
            'email': create_random_email(),
            'password': create_random_password(),
            'name': create_random_username()
        }
        response = requests.patch(Urls.USER_UPDATE, headers=Urls.HEADERS,  json = data)
        assert response.json() == ReqText.WITHOUT_AUTH