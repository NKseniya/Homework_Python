import uuid

from api_client import ProjectsApi


def assert_status(response, expected):
    """Проверка кода ответа с понятным сообщением при падении."""
    message = (
        f"Ожидался код {expected}, "
        f"получено: {response.status_code}, {response.text}"
    )
    assert response.status_code == expected, message


# ---------- POST /api-v2/projects ----------

def test_create_project_positive(api: ProjectsApi):
    """Позитивный: проект с валидным title создаётся, код 201."""
    title = f"autotest-create-{uuid.uuid4()}"
    response = api.create({"title": title})
    assert_status(response, 201)
    assert "id" in response.json(), "id проекта отсутствует в ответе"
    # прибираемся за собой
    api.update(response.json()["id"], {"deleted": True, "title": title})


def test_create_project_without_title_negative(api: ProjectsApi):
    """Негативный: создание без обязательного поля title — ошибка 400."""
    response = api.create({"description": "проект без названия"})
    assert_status(response, 400)


def test_create_project_invalid_token_negative():
    """Негативный: запрос с неверным токеном — ошибка 401."""
    broken_client = ProjectsApi(token="invalid-token-000")
    response = broken_client.create({"title": f"autotest-neg-{uuid.uuid4()}"})
    assert_status(response, 401)


# ---------- PUT /api-v2/projects/{id} ----------

def test_update_project_positive(api: ProjectsApi, created_project):
    """Позитивный: переименование существующего проекта, код 200."""
    new_title = f"autotest-renamed-{uuid.uuid4()}"
    response = api.update(created_project, {"title": new_title})
    assert_status(response, 200)


def test_update_nonexistent_project_negative(api: ProjectsApi):
    """Негативный: изменение несуществующего проекта — ошибка 404."""
    response = api.update(uuid.uuid4(), {"title": "не существует"})
    assert_status(response, 404)


# ---------- GET /api-v2/projects/{id} ----------

def test_get_project_positive(api: ProjectsApi, created_project):
    """Позитивный: полученный проект совпадает с созданным, код 200."""
    response = api.get_by_id(created_project)
    assert_status(response, 200)
    project = response.json()
    assert project["id"] == created_project
    assert project["deleted"] is False


def test_get_nonexistent_project_negative(api: ProjectsApi):
    """Негативный: запрос несуществующего проекта — ошибка 404."""
    response = api.get_by_id(uuid.uuid4())
    assert_status(response, 404)


def test_get_project_without_auth_negative():
    """Негативный: GET без токена авторизации — ошибка 401."""
    no_auth = ProjectsApi(token="")
    response = no_auth.get_by_id(uuid.uuid4())
    assert_status(response, 401)
