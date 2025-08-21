# db_init/company/seed_company.py

from db_init.session import SessionLocal
import db_init.new_vessel_proj.crud as repos
from datetime import datetime


# пользователи компании
def seed_users():
    session = SessionLocal()
    try:
        users_data = [
            ("hull1", "hulldept@adomat.ru", "Алексей Анатольевич", "Дмитриев", "+000000000", True, datetime(2014, 3, 15), [12345], ["Соучредитель"], ["Отдел корпус"]),
            ("hull2", "hulldept2@adomat.ru", "Максим Евгеньевич", "Федюнин", "+000000000", True, datetime(2014, 9, 8), [12345], ["Специалист"], ["Отдел корпус"]),
            ("hull3", "docdept@adomat.ru", "Ольга Леонидовна", "Сербовка", "+000000000", True, datetime(2015, 5, 18), [12345], ["Специалист"], ["Отдел корпус"]),
            ("hull4", "hulldept3@adomat.ru", "Артем Дмитриев", "Сергеев", "+000000000", True, datetime(2024, 8, 12), [12345], ["Специалист"], ["Отдел корпус"]),
            ("hull5", "hulldept4@adomat.ru", "Валерия Романовна", "Макарова", "+0000000000", True, datetime(2025, 4, 7), [12345], ["Специалист"], ["Отдел корпус"]),
            ("mech1", "mechdept@adomat.ru", "Андрей Николаевич", "Титов", "+0000000000", True, datetime(2014, 3, 15), [12345], ["Соучредитель"], ["Отдел механика"]),
            ("mech2", "mechdept2@adomat.ru", "Виталий Александрович", "Дубинин", "+0000000000", True, datetime(2018, 3, 21), [12345], ["Ведущий специалист"], ["Отдел механика"]),
            ("mech3", "mechdept3@adomat.ru", "Владимир Олегович", "Власов", "+0000000000", True, datetime(2021, 1, 9), [12345], ["Специалист"], ["Отдел механика"]),
            ("el1", "eldept@adomat.ru", "Андрей Анатольевич", "Михин", "+0000000000", True, datetime(2016, 4, 1), [12345], ["Специалист"], ["Отдел электрика"]),
            ("el2", "eldept2@adomat.ru", "Андрей Иванович", "Евстратов", "+0000000000", True, datetime(2021, 11, 1), [12345], ["Специалист"], ["Отдел электрика"]),
            ("el3", "eldept3@adomat.ru", "Сергей Александрович", "Райкевич", "+0000000000", True, datetime(2019, 6, 5), [12345], ["Ведущий специалист"], ["Отдел электрика"]),
            ("aup1", "o.martens@bk.ru", "Олег Иванович", "Мартенс", "+0000000000", True, datetime(2025, 4, 7), [12345], ["Соучредитель"], ["АУП"]),
            ("aup2", "pm@adomat.ru", "Дмитрий Казимирович", "Семуха", "+0000000000", True, datetime(2025, 4, 7), [12345], ["Проектный офис"], ["АУП"]),
            ("aup3", "d.grigorev@adomat.ru", "Денис Александрович", "Григорьев", "+0000000000", True, datetime(2025, 4, 7), [12345], ["Экономист"], ["АУП"])
        ]

        repo = repos.UserRepository(session)
        for username, email, first_name, last_name, phone, is_active, date_of_employment, password_hash, roles, deps in users_data:
            repo.create_or_update_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                is_active=is_active,
                date_of_employment=date_of_employment,
                password_hash="12345",
                roles=roles,
                departments=deps
            )

        session.commit()
        print("✔️ Таблица users заполнена данными")
    except Exception as e:
        session.rollback()
        print(f"❌ Ошибка при заполнении users: {e}")
        raise
    finally:
        session.close()

# отделы компании
def seed_departments() -> None:
    """
    Наполняет таблицу departments начальными данными.
    """
    session = SessionLocal()
    try:
        # Список отделов компании
        types_data = [
            ("АУП", "Административно-управленческий персонал"),
            ("Отдел корпус", ""),
            ("Отдел механика", ""),
            ("Отдел электрика", "")
        ]
        repo = repos.DepartmentRepository(session)
        for name, desc in types_data:
            repo.create_department(name, desc)

        session.commit()
        print("✔️ Таблица departments заполнена данными")
    except Exception as e:
        session.rollback()
        print(f"❌ Ошибка при заполнении departments: {e}")
        raise
    finally:
        session.close()

# роли в компании
def seed_roles() -> None:
    """
    Наполняет таблицу roles начальными данными.
    """
    session = SessionLocal()
    try:
        # Список ролей
        types_data = [
            ("Администратор", ""),
            ("Директор", ""),
            ("Соучредитель", ""),
            ("Проектный офис", ""),
            ("Бухгалтер", ""),
            ("Экономист", ""),
            ("Ведущий специалист", ""),
            ("Специалист", ""),
            ("Стажер", ""),
            ("Клиент", ""),
            ("Контрагент", ""),
            ("Гость", ""),
            ("Соискатель", ""),
        ]
        repo = repos.RoleRepository(session)
        for name, desc in types_data:
            repo.create_role(name, desc)

        session.commit()
        print("✔️ Таблица roles заполнена данными")
    except Exception as e:
        session.rollback()
        print(f"❌ Ошибка при заполнении roles: {e}")
        raise
    finally:
        session.close()
