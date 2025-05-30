# scripts/seed.py
# Скрипт наполнения базовых данных (seeding) 🌱

from db.session import SessionLocal
from db.crud import ProjTypeRepository, VesselTypeRepository, ClassSocietyRepository


def seed_proj_types() -> None:
    """
    Наполняет таблицу proj_type начальными данными.
    """
    session = SessionLocal()
    try:
        # Список типов проектов для вставки
        types_data = [
            ("НОВОЕ СУДНО", "Проекты новых судов"),
            ("ПЕРЕОБОРУДОВАНИЕ", "Проекты переоборудования судов"),
            ("РАЗВИТИЕ", "Проекты, направленные на развитие компании"),
            ("АДМИНИСТРАТИВКА", "Проект для учета административных потерь времени"),
        ]
        repo = ProjTypeRepository(session)
        for name, desc in types_data:
            repo.create_proj_types(name, desc)

        session.commit()
        print("✔️ Таблица proj_type заполнена данными")
    except Exception as e:
        session.rollback()
        print(f"❌ Ошибка при заполнении proj_type: {e}")
        raise
    finally:
        session.close()

def seed_vessel_types() -> None:
    """
    Наполняет таблицу vessel_type начальными данными.
    """
    session = SessionLocal()
    try:
        # Список типов судов для вставки
        types_data = [
            ("00. АДОМАТ", ""),
            ("00. СЕРИИ СУДОВ", ""),
            ("01. НЕФТЕНАЛИВНЫЕ", ""),
            ("02. НЕФТЕНАЛИВНЫЕ - ХИМОВОЗЫ", ""),
            ("03. ХИМОВОЗЫ", ""),
            ("04. ГАЗОВОЗЫ", ""),
            ("05. НАЛИВНЫЕ ПРОЧИЕ", ""),
            ("06. НЕФТЕНАВАЛОЧНЫЕ И НЕФТЕРУДОВОЗЫ", ""),
            ("07. РУДОВОЗЫ И НАВАЛОЧНЫЕ", ""),
            ("08. СУДА ДЛЯ ГЕНГРУЗА", ""),
            ("09. ГРУЗОПАССАЖИРСКИЕ", ""),
            ("10. КОНТЕЙНЕРНЫЕ, БАРЖЕВОЗЫ, ДОКОВЫЕ", ""),
            ("11. СУДА ДЛЯ ПЕРЕВОЗКИ ТРАНСПОРТНЫХ СРЕДСТВ", ""),
            ("12. РЫБОПРОМЫСЛОВЫЕ БАЗЫ, РЫБОТРАНСПОРТНЫЕ СУДА", ""),
            ("13.1 РЫБОПРОМЫСЛОВЫЕ более 45 м", ""),
            ("13.2 РЫБОПРОМЫСЛОВЫЕ менее 45 м", ""),
            ("14. ПАССАЖИРСКИЕ И ПАССАЖИРСКИЕ БЕСКОЕЧНЫЕ", ""),
            ("15. СУДА ОБЕСПЕЧЕНИЯ", ""),
            ("16. БУКСИРЫ", ""),
            ("17. ЗЕМСНАРЯДЫ И ЗЕМЛЕСОСЫ", ""),
            ("18. РЕФРИЖЕРАТОРНЫЕ", ""),
            ("19. ЛЕДОКОЛЫ", ""),
            ("20. НАУЧНО-ИССЛЕДОВАТЕЛЬСКИЕ", ""),
            ("21. ПРОЧИЕ", ""),
            ("22. МАЛОМЕРНЫЕ, ПРОГУЛОЧНЫЕ", ""),
            ("24. ПАРУСНЫЕ, УЧЕБНЫЕ", ""),
        ]
        repo = VesselTypeRepository(session)
        for name, desc in types_data:
            repo.create_vessel_types(name, desc)

        session.commit()
        print("✔️ Таблица vessel_type заполнена данными")
    except Exception as e:
        session.rollback()
        print(f"❌ Ошибка при заполнении vessel_type: {e}")
        raise
    finally:
        session.close()

def seed_class_societys() -> None:
    """
    Наполняет таблицу class_societys начальными данными.
    """
    session = SessionLocal()
    try:
        # Список Классификационных обществ
        types_data = [
            ("01. РС", "Российский Морской Регистр Судоходства"),
            ("02. РКО", "Российское Классификационное общество"),
            ("03. Прочее", "Прочие Классификационные общества"),
        ]
        repo = ClassSocietyRepository(session)
        for name, desc in types_data:
            repo.create_class_society_name(name, desc)

        session.commit()
        print("✔️ Таблица class_societys заполнена данными")
    except Exception as e:
        session.rollback()
        print(f"❌ Ошибка при заполнении class_societys: {e}")
        raise
    finally:
        session.close()


if __name__ == "__main__":
    seed_proj_types()
    seed_vessel_types()
    seed_class_societys()
