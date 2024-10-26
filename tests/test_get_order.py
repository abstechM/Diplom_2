from conftest import *
import requests
import allure


class TestGetOrders:
    @allure.title('Тест получения списка заказов с авторизованным пользователем')
    def test_get_orders_auth(self, create_user_and_order_and_delete):
        headers = {'Authorization': create_user_and_order_and_delete[0]}
        response = requests.get(Urls.GET_USER_ORDERS, headers=headers)
        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Тест получения списка заказов с авторизованным пользователем')
    def test_get_orders_without_auth(self):
        response = requests.get(Urls.GET_USER_ORDERS, headers=Urls.HEADERS)
        assert response.status_code == 401
        assert response.json() == ReqText.WITHOUT_AUTH