import requests
import pytest

# Замените на ваш реальный токен и URL (если используете коробку)
BASE_URL = "https://yougile.com"
TOKEN = "ВАШ_ТОКЕН_ЗДЕСЬ" 

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

@pytest.fixture(scope="module")
def project_context():
    """Фикстура для хранения ID созданного проекта между тестами."""
    context = {"id": None}
    return context

def test_create_project(project_context):
    """Тест создания проекта [POST]"""
    payload = {
        "title": "New Project by Autotest"
    }
    response = requests.post(BASE_URL, json=payload, headers=HEADERS)
    
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["title"] == payload["title"]
    
    project_context["id"] = data["id"]

def test_get_project_by_id(project_context):
    """Тест получения проекта [GET]"""
    p_id = project_context["id"]
    assert p_id is not None, "Project ID is missing"
    
    response = requests.get(f"{BASE_URL}/{p_id}", headers=HEADERS)
    
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == p_id
    assert "title" in data

def test_update_project(project_context):
    """Тест изменения названия проекта [PUT]"""
    p_id = project_context["id"]
    assert p_id is not None, "Project ID is missing"
    
    payload = {
        "title": "Updated Project Title"
    }
    response = requests.put(f"{BASE_URL}/{p_id}", json=payload, headers=HEADERS)
    
    assert response.status_code == 200
    
    # Дополнительная проверка через GET
    check_response = requests.get(f"{BASE_URL}/{p_id}", headers=HEADERS)
    assert check_response.json()["title"] == "Updated Project Title"

def test_create_project_invalid_auth():
    """Негативный тест: проверка авторизации"""
    bad_headers = {"Authorization": "Bearer INVALID", "Content-Type": "application/json"}
    response = requests.get(BASE_URL, headers=bad_headers)
    assert response.status_code in [401, 403]
