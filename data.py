from helpers import *



class UserData:
    EMAIL = 'gismo513@mail.ru'
    PASSWORD = '123456789'
    USER_NAME = 'Alexander'

class EmptyField:
    EMPTY_EMAIL = {
        'password': create_random_password(),
        'name': create_random_username()
    }
    EMPTY_PSWD = {
        'email': create_random_email(),
        'name': create_random_username()
    }
    EMPTY_NAME = {
        'email': create_random_email(),
        'password': create_random_password()
    }
class Burger:
    CORRECT_HASH = ["61c0c5a71d1f82001bdaaa6c","61c0c5a71d1f82001bdaaa75"]
    WRONG_HASH = ['61c0c5a71d1f8775fg657464']
    ERROR_HASH = 'Internal Server Error'


class ReqText:
    REPEAT_REG = {"success": False,"message": "User already exists"}
    ERROR_EMPTY_FIELD = {"success": False,"message": "Email, password and name are required fields"}
    WRONG_EMAIL_AND_PSWD = {"success": False,"message": "email or password are incorrect"}
    WITHOUT_AUTH = {"success": False,"message": "You should be authorised"}
    TEXT_ERROR_HASH = {"success": False,"message": "Ingredient ids must be provided"}
    RESET_PSWD = {"success": True,"message": "Reset email sent"}

