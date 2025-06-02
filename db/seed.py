# scripts/seed.py
# Скрипт наполнения базовых данных (seeding) 🌱

from db.session import SessionLocal
from db.crud import (ProjTypeRepository, VesselTypeRepository, ClassSocietyRepository, NewLifeCycleRepository,
                     RefitLifeCycleRepository, ProjTemplateRepository)


def seed_proj_types() -> None:
    """
    Наполняет таблицу proj_type начальными данными.
    """
    session = SessionLocal()
    try:
        # Список типов проектов для вставки
        types_data = [
            ("00. НОВОЕ СУДНО", "Проекты новых судов"),
            ("01. ПЕРЕОБОРУДОВАНИЕ", "Проекты переоборудования судов"),
            ("02. РАЗВИТИЕ", "Проекты, направленные на развитие компании"),
            ("03. АДМИНИСТРАТИВКА", "Проект для учета административных потерь времени"),
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

def seed_new_life_cycle() -> None:
    """
    Наполняет таблицу new_lify_cycle начальными данными.
    """
    session = SessionLocal()
    try:
        # Список жизненных циклов проекта нового судна
        types_data = [
            ("01. ТП", "Технический проект"),
            ("02. КП", "Концепт-проект"),
            ("03. ПДСП", "Проектная документация судна в постройке"),
            ("04. РКД", "Рабоче-конструкторская документация"),
            ("05. ПСД", "Приемо-сдаточная документация"),
            ("06. ЭД", "Эксплуатационная документация"),
            ("07. АРХИВ", "Все закрывающие документы и архив проекта"),
        ]
        repo = NewLifeCycleRepository(session)
        for name, desc in types_data:
            repo.create_new_life_cycle_name(name, desc)

        session.commit()
        print("✔️ Таблица new_life_cycle заполнена данными")
    except Exception as e:
        session.rollback()
        print(f"❌ Ошибка при заполнении new_life_cycle: {e}")
        raise
    finally:
        session.close()

def seed_refit_life_cycle() -> None:
    """
    Наполняет таблицу refit_life_cycle начальными данными.
    """
    session = SessionLocal()
    try:
        # Список жизненных циклов проекта переоборудования
        types_data = [
            ("01. ИНИЦИАЦИЯ", "Вся работа по определению трудозатрат проекта"),
            ("02. ДОГОВОР", "На основании трудозатрат оформление Коммерческого предложения и договора"),
            ("03. РАБОТА", "После подтверждения договора работа над проектом"),
            ("04. ЗАКАЗЧИК", "Согласование проекта с Заказчиком"),
            ("05. КЛАССИФИКАЦИОННОЕ ОБЩЕСТВО", "Согласование проекта с Классификационным обществом (при необходимости)"),
            ("06. ОПЛАТА", "Проект на этапе оплаты Заказчиком"),
            ("07. АРХИВ", "Проект в архив"),
        ]
        repo = RefitLifeCycleRepository(session)
        for name, desc in types_data:
            repo.create_refit_life_cycle_name(name, desc)

        session.commit()
        print("✔️ Таблица new_life_cycle заполнена данными")
    except Exception as e:
        session.rollback()
        print(f"❌ Ошибка при заполнении new_life_cycle: {e}")
        raise
    finally:
        session.close()

def seed_proj_template() -> None:
    """
    Наполняет таблицу proj_template начальными данными.
    """
    session = SessionLocal()
    try:
        # Список шаблонов проектов
        types_data = [
            ("План противопожарной защиты и спасательных средств", "FIRE & SAFETY PLAN", "Подлежит рассмотрению",
             "\\192.168.1.98\02 Library\00 Шаблоны\XXXXX.360089.001 FIRE & SAFETY PLAN",
             "Согласно требований SOLAS-74, Chapter II-2, Regulation 15 Р.2.4"),
            ("", "", "", "","")
        ]
        repo = ProjTemplateRepository(session)
        for name_ru, name_en, reviewed, path, desc in types_data:
            repo.create_proj_template(name_ru, name_en, reviewed, path, desc)

        session.commit()
        print("✔️ Таблица proj_template заполнена данными")
    except Exception as e:
        session.rollback()
        print(f"❌ Ошибка при заполнении proj_template: {e}")
        raise
    finally:
        session.close()


if __name__ == "__main__":
    seed_proj_types()
    seed_vessel_types()
    seed_class_societys()
    seed_new_life_cycle()
    seed_refit_life_cycle()
    seed_proj_template()
