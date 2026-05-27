import pytest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Подключение к БД 
DATABASE_URL = "postgresql://postgres:1111@localhost:5432/QA_NATA"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# 2. Модель таблицы
class Student(Base):
    __tablename__ = "student"

    user_id = Column(Integer, primary_key=True)
    level = Column(String)
    education_form = Column(String)
    subject_id = Column(Integer)


# 3. Фикстура для автоматической очистки данных 
@pytest.fixture
def db_session():
    session = SessionLocal()
    yield session
    # После каждого теста откатываем изменения и закрываем сессию
    session.rollback()
    session.close()


# ==================== ТЕСТЫ ====================

# Тест 1: Добавление сущности (Student)
def test_add_student(db_session):
    # Создаем объект нового студента (id=999, которого нет в БД)
    new_student = Student(user_id=999, level="Начальный", education_form="Онлайн", subject_id=1)
    
    db_session.add(new_student)
    db_session.commit()  # Сохраняем в базу

    # Проверяем, что студент успешно добавился
    db_student = db_session.query(Student).filter_by(user_id=999).first()
    assert db_student is not None
    assert db_student.level == "Начальный"

    # Очистка: удаляем созданного студента
    db_session.delete(db_student)
    db_session.commit()


# Тест 2: Изменение сущности (Student)
def test_update_student(db_session):
    # Сначала создаем студента для теста
    student = Student(user_id=998, level="Средний", education_form="Оффлайн", subject_id=2)
    db_session.add(student)
    db_session.commit()

    # Изменяем форму обучения
    student.education_form = "Вечерняя"
    db_session.commit()

    # Проверяем, что изменения применились
    updated_student = db_session.query(Student).filter_by(user_id=998).first()
    assert updated_student.education_form == "Вечерняя"

    # Очистка: удаляем за собой данные
    db_session.delete(updated_student)
    db_session.commit()


# Тест 3: Удаление сущности (Student)
def test_delete_student(db_session):
    # Сначала создаем студента, которого будем удалять
    student = Student(user_id=997, level="Продвинутый", education_form="Онлайн", subject_id=3)
    db_session.add(student)
    db_session.commit()

    # Удаляем его из базы
    db_session.delete(student)
    db_session.commit()

    # Проверяем, что его больше нет в БД
    deleted_student = db_session.query(Student).filter_by(user_id=997).first()
    assert deleted_student is None
