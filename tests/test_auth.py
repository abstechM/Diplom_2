import requests
from conftest import *
import allure


class TestLogin:
    @allure.title('Тест авторизации с неверным паролем')
    def test_login_with_wrong_pswd(self):
        payload = {
            'email': UserData.EMAIL,
            'password': create_random_password(),
        }
        response = requests.post(Urls.USER_LOGIN, data=payload)
        assert response.status_code == 401
        assert response.json() == ReqText.WRONG_EMAIL_AND_PSWD

    @allure.title('Тест автоизации с неверным email')
    def test_login_with_wrong(self):
        payload = {
            'email': create_random_email(),
            'password': UserData.PASSWORD,
        }
        response = requests.post(Urls.USER_LOGIN, data=payload)
        assert response.status_code == 401
        assert response.json() == ReqText.WRONG_EMAIL_AND_PSWD

    @allure.title('Тест успешной авторизации')
    def test_auth_success(self, create_new_user_and_delete):
        payload = create_new_user_and_delete[0]
        response = requests.post(Urls.USER_LOGIN, data=payload)
        assert response.status_code == 200
        assert response.json()['success'] is True
        assert response.json()['user']['email'] == create_new_user_and_delete[0]['email']
        assert response.json()['user']['name'] == create_new_user_and_delete[0]['name']

    @allure.title('Тест сброса пароля')
    def test_reset_pswd(self, create_new_user_and_delete):
        payload = create_new_user_and_delete[0]
        response = requests.post(Urls.USER_LOGIN, data=payload)
        assert response.status_code == 200
        response = requests.post(Urls.USER_RESET, data=payload)
        assert response.status_code == 200
        assert response.json() == ReqText.RESET_PSWD




