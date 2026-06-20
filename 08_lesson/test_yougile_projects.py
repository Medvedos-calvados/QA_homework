import pytest

# Позитивный и негативный тесты на POST
def test_create_project_positive(api):
    payload = {"title": "Новый проект Skypro", "users": {}}
    response = api.create_project(payload)
    assert response.status_code == 201
    assert "id" in response.json()

def test_create_project_negative_empty_title(api):
    payload = {"users": {}}
    response = api.create_project(payload)
    assert response.status_code == 400

# Позитивный и негативный тесты на GET
def test_get_project_positive(api):
    create_res = api.create_project({"title": "Временный GET", "users": {}}).json()
    project_id = create_res["id"]

    response = api.get_project(project_id)
    assert response.status_code == 200
    assert response.json()["title"] == "Временный GET"

def test_get_project_negative_wrong_id(api):
    response = api.get_project("00000000-0000-0000-0000-000000000000")
    assert response.status_code == 404

# Позитивный и негативный тесты на PUT
def test_update_project_positive(api):
    create_res = api.create_project({"title": "Проект до PUT", "users": {}}).json()
    project_id = create_res["id"]

    payload = {"title": "Обновленный проект"}
    response = api.update_project(project_id, payload)
    assert response.status_code == 200
    assert response.json()["id"] == project_id

def test_update_project_negative_invalid_id(api):
    payload = {"title": "Новое название"}
    response = api.update_project("00000000-0000-0000-0000-000000000000", payload)
    assert response.status_code == 404
