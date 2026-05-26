import pytest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker


# подключение к базе данных
DATABASE_URL = "postgresql://postgres:1111@localhost:5432/QA_NATA"

# Настройка SQLAlchemy
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)


# Структура таблицы "student"
class Student(Base):
    __tablename__ = "student"

    user_id = Column(Integer, primary_key=True)
    level = Column(String)
    education_form = Column(String)
    subject_id = Column(Integer)


# --- ТЕСТЫ ---


# Тест 1: Добавление студента
def test_add_student():
    session = Session()

    
    new_student = Student(
        user_id=9999,
        level="Бакалавриат",
        education_form="Очная",
        subject_id=1,
    )
    session.add(new_student)
    session.commit()

    # ПРОВЕРКА: ищем добавленного студента в БД
    student_in_db = session.query(Student).filter_by(user_id=9999).first()
    assert student_in_db is not None
    assert student_in_db.level == "Бакалавриат"

    # ОЧИСТКА ЗА СОБОЙ 
    session.delete(student_in_db)
    session.commit()
    session.close()


# Тест 2: Изменение данных студента
def test_update_student():
    session = Session()

    # Создаем данные для теста
    student = Student(
        user_id=9998, level="Магистратура", education_form="Заочная", subject_id=2
    )
    session.add(student)
    session.commit()

    # Изменяем форму обучения
    student.education_form = "Очно-заочная"
    session.commit()

    # ПРОВЕРКА: смотрим изменения в БД
    updated_student = session.query(Student).filter_by(user_id=9998).first()
    assert updated_student.education_form == "Очно-заочная"

    # ОЧИСТКА ЗА СОБОЙ
    session.delete(updated_student)
    session.commit()
    session.close()


# Тест 3: Удаление студента
def test_delete_student():
    session = Session()

    # Создаем временного студента
    student = Student(
        user_id=9997, level="Аспирантура", education_form="Очная", subject_id=3
    )
    session.add(student)
    session.commit()

    # Удаляем его из БД
    session.delete(student)
    session.commit()

    # ПРОВЕРКА: проверяем, что его больше нет в базе
    deleted_student = session.query(Student).filter_by(user_id=9997).first()
    assert deleted_student is None
    session.close()