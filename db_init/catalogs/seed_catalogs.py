# db_init/catalogs/seed_catalogs.py

from db_init.session import SessionLocal
import db_init.catalogs.crud_catalogs as repos


# тип судна
def seed_vessel_types() -> None:
    """
    Наполняет таблицу vessel_type начальными данными.
    """
    session = SessionLocal()
    try:
        # Список типов судов
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
        repo = repos.VesselTypeRepository(session)
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

# классификационное общество
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
        repo = repos.ClassSocietyRepository(session)
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

# статус проекта
def seed_proj_status() -> None:
    """
    Наполняет таблицу proj_status начальными данными.
    """
    session = SessionLocal()
    try:
        # Список статусов проекта нового судна
        types_data = [
            ("не начат", ""),
            ("в работе", ""),
            ("отложен", ""),
            ("отменен", "")
        ]
        repo = repos.ProjStatusRepository(session)
        for name, desc in types_data:
            repo.create_proj_status(name, desc)

        session.commit()
        print("✔️ Таблица new_proj_status заполнена данными")
    except Exception as e:
        session.rollback()
        print(f"❌ Ошибка при заполнении new_proj_status: {e}")
        raise
    finally:
        session.close()
