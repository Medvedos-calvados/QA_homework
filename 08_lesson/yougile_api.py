import requests
from config import BASE_URL, TOKEN

class YougileApi:
    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json"
        }

    def create_project(self, title, users=None):
        payload = {"title": title}
        if users:
            payload["users"] = users
        return requests.post(f"{BASE_URL}/projects", json=payload, headers=self.headers)

    def get_project(self, project_id):
        return requests.get(f"{BASE_URL}/projects/{project_id}", headers=self.headers)

    def update_project(self, project_id, new_title):
        payload = {"title": new_title}
        return requests.put(f"{BASE_URL}/projects/{project_id}", json=payload, headers=self.headers)
