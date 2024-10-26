import requests
from conftest import *
import allure


class TestOrder:
    @allure.title('Тест заказа с авторизованым пользователем')
    def test_succes_order_auth(self, create_new_user_and_delete):
        headers = {'Authorization': create_new_user_and_delete[1]['accessToken']}
        payload = {'ingredients': [Burger.CORRECT_HASH]}
        response = requests.post(Urls.URL_ORDER, data=payload, headers=headers)
        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Тест заказа неавторизованым пользователем')
    def test_succes_order_without_auth(self):
        payload = {'ingredients': [Burger.CORRECT_HASH]}
        response = requests.post(Urls.URL_ORDER, data=payload)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title('Тест заказа с пустым значением ингредиентов авторизованным пользователем')
    def test_order_epmpty_ingredient_auth(self, create_new_user_and_delete):
        headers = {'Authorization': create_new_user_and_delete[1]['accessToken']}
        payload = {'ingredients': []}
        response = requests.post(Urls.URL_ORDER, data=payload, headers=headers)
        assert response.status_code == 400
        assert response.json() == ReqText.TEXT_ERROR_HASH

    @allure.title('Тест заказа с пустым значением ингредиентов c неавторизованным пользователем')
    def test_oreder_epmpty_ingredient_without_auth(self):
        payload = {'ingredients': []}
        response = requests.post(Urls.URL_ORDER, data=payload, headers=Urls.HEADERS)
        assert response.status_code == 400
        assert response.json() == ReqText.TEXT_ERROR_HASH

    @allure.title('Тест неверного ХЭШ ингредиентов c авторизованным пользователм')
    def test_order_wrong_hash_auth(self, create_new_user_and_delete):
        headers = {'Authorization': create_new_user_and_delete[1]['accessToken']}
        payload = {'ingredients': [Burger.WRONG_HASH]}
        response = requests.post(Urls.URL_ORDER, data=payload, headers=headers)
        assert response.status_code == 500
        assert Burger.ERROR_HASH in response.text