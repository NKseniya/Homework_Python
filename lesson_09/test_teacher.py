import uuid

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
import pytest

load_dotenv()
db_connection_string = (
    "postgresql+psycopg2://postgres:Qa123456@localhost:5432/QA"
)
db = create_engine(db_connection_string)

TABLE = "teacher"
ID_COLUMN = "teacher_id"


# ---------- вспомогательные функции ----------

def add_teacher(email, group_id):
    """Добавляет преподавателя с новым id и возвращает его id."""
    with db.connect() as conn:
        new_id = conn.execute(
            text("SELECT COALESCE(MAX(teacher_id), 0) + 1 FROM teacher")
        ).scalar_one()
        conn.execute(
            text(
                "INSERT INTO teacher (teacher_id, email, group_id) "
                "VALUES (:id, :email, :group_id)"
            ),
            {"id": new_id, "email": email, "group_id": group_id},
        )
        conn.commit()
        return new_id


def get_teacher(teacher_id):
    """Возвращает словарь с данными преподавателя или None."""
    sql = text(f"SELECT * FROM {TABLE} WHERE {ID_COLUMN} = :id")
    with db.connect() as conn:
        row = conn.execute(sql, {"id": teacher_id}).mappings().first()
        return dict(row) if row else None


def update_teacher(teacher_id, new_email):
    """Меняет email преподавателя."""
    sql = text(
        f"UPDATE {TABLE} SET email = :email WHERE {ID_COLUMN} = :id"
    )
    with db.connect() as conn:
        conn.execute(sql, {"id": teacher_id, "email": new_email})
        conn.commit()


def delete_teacher(teacher_id):
    """Удаляет преподавателя."""
    sql = text(f"DELETE FROM {TABLE} WHERE {ID_COLUMN} = :id")
    with db.connect() as conn:
        conn.execute(sql, {"id": teacher_id})
        conn.commit()


# ---------- фикстура ----------

@pytest.fixture
def new_teacher():
    """Создаёт преподавателя, после теста удаляет его из БД."""
    email = f"autotest-{uuid.uuid4()}@example.com"
    teacher_id = add_teacher(email, 1)
    yield teacher_id
    delete_teacher(teacher_id)


# ---------- тесты ----------

def test_add_teacher():
    """Добавление: преподаватель создан и читается из БД."""
    email = f"autotest-add-{uuid.uuid4()}@example.com"
    teacher_id = None
    try:
        teacher_id = add_teacher(email, 1)
        teacher = get_teacher(teacher_id)
        assert teacher is not None, "Преподаватель не найден после создания"
        assert teacher["email"] == email
    finally:
        if teacher_id is not None:
            delete_teacher(teacher_id)


def test_update_teacher(new_teacher):
    """Изменение: email обновляется в БД."""
    new_email = f"autotest-upd-{uuid.uuid4()}@example.com"
    update_teacher(new_teacher, new_email)
    teacher = get_teacher(new_teacher)
    assert teacher["email"] == new_email, (
        f"Email не изменился: {teacher}"
    )


def test_delete_teacher():
    """Удаление: строка исчезает из БД."""
    email = f"autotest-del-{uuid.uuid4()}@example.com"
    teacher_id = add_teacher(email, 1)
    delete_teacher(teacher_id)
    assert get_teacher(teacher_id) is None, "Преподаватель не удалился"
