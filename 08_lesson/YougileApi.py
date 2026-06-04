import requests

class YougileApi:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url.rstrip('/')
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create_project(self, payload: dict) -> requests.Response:
        """[POST] /api-v2/projects — Создание проекта"""
        return requests.post(f"{self.base_url}/api-v2/projects", json=payload, headers=self.headers)

    def get_project(self, project_id: str) -> requests.Response:
        """[GET] /api-v2/projects/{id} — Получение проекта по ID"""
        return requests.get(f"{self.base_url}/api-v2/projects/{project_id}", headers=self.headers)

    def update_project(self, project_id: str, payload: dict) -> requests.Response:
        """[PUT] /api-v2/projects/{id} — Изменение проекта по ID"""
        return requests.put(f"{self.base_url}/api-v2/projects/{project_id}", json=payload, headers=self.headers)
