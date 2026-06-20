import pytest
from YougileApi import YougileApi

BASE_URL = "https://yougile.com"
TOKEN = "СЮДА_НУЖНО_ВСТАВИТЬ_ТОКЕН"

@pytest.fixture(scope="session")
def api():
    """Инициализация клиента на всю сессию тестов."""
    return YougileApi(BASE_URL, TOKEN)
