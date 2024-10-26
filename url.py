class Urls:
    URL = 'https://stellarburgers.nomoreparties.site'
    USER_REGISTER = f'{URL}/api/auth/register'
    USER_LOGIN = f'{URL}/api/auth/login'
    URL_ORDER = f'{URL}/api/orders'
    USER_RESET = f'{URL}/api/password-reset'
    USER_UPDATE = f'{URL}/api/auth/user'
    USER_DELETE = f'{URL}/api/auth/user'
    GET_USER_ORDERS = f'{URL}/api/orders'
    HEADERS = {'Content-Type': 'application/json'}