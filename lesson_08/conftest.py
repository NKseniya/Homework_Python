import uuid

import pytest

from api_client import ProjectsApi


@pytest.fixture
def api():
    return ProjectsApi()


@pytest.fixture
def created_project(api):
    """Создаёт проект с уникальным названием, после теста удаляет его."""
    title = f"autotest-{uuid.uuid4()}"
    response = api.create({"title": title})
    assert response.status_code == 201, (
        f"Не удалось создать проект: {response.text}")
    project_id = response.json()["id"]
    yield project_id
    # Удаление через PUT с флагом deleted — у Yougile нет DELETE для проектов
    api.update(project_id, {"deleted": True, "title": title})
