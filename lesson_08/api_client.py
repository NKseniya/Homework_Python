import requests

from config import BASE_URL, TOKEN


class ProjectsApi:
    """Обёртка над методами /api-v2/projects (Page Object для API)."""

    def __init__(self, base_url=BASE_URL, token=TOKEN):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        })

    def create(self, payload):
        """POST /api-v2/projects — создание проекта."""
        return self.session.post(f"{self.base_url}/projects", json=payload)

    def update(self, project_id, payload):
        """PUT /api-v2/projects/{id} — изменение проекта."""
        return self.session.put(
            f"{self.base_url}/projects/{project_id}", json=payload
            )

    def get_by_id(self, project_id):
        """GET /api-v2/projects/{id} — получение проекта."""
        return self.session.get(f"{self.base_url}/projects/{project_id}")
