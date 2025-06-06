# scripts/seed.py
# Скрипт наполнения базовых данных (seeding) 🌱

from db_init.session import SessionLocal
from db_init.crud import (ProjTypeRepository, VesselTypeRepository, ClassSocietyRepository, NewLifeCycleRepository,
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
        print("✔️ Таблица refit_life_cycle заполнена данными")
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
            # ОБЩИЕ
            (
                "Общие",
                "Проект нового судна",
                "NEW SHEEP",
                "Подлежит рассмотрению",
                r"\\192.168.1.98\02 Library\00 Шаблоны\00 Проект нового судна",
                "Согласно ТЗ на проектирование, в соответствии с Правилами, конвенциями и Нормами"
            ),
            (
                "Общие",
                "Проект переоборудования",
                "REFIT",
                "",
                r"\\192.168.1.98\02 Library\00 Шаблоны\10 Проект переоборудования",
                "Согласно ТЗ на проектирование, в соответствии с Правилами, конвенциями и Нормами"
            ),
            # 03 УСТРОЙСТВА, ОБОРУДОВАНИЕ И СНАБЖЕНИЕ
            (
                "03 Устройства, оборудование и снабжение",
                "(MSMP) План управления системой швартовки",
                "(MSMP) Mooring system management plan",
                "Не подлежит рассмотрению",
                r"\\192.168.1.98\02 Library\00 Шаблоны\089.001 (MSMP) План ПУСС",
                "Согласно MARPOL Annex I, OCIMF – для танкеров"
            ),
            (
                "03 Устройства, оборудование и снабжение",
                "(STS) План по перекачке груза нефти с судна на судно",
                "(STS) Ship to ship oil cargo transfer operations plan",
                "Подлежит рассмотрению",
                r"\\192.168.1.98\02 Library\00 Шаблоны\089.002 (STS) План ПГНСС",
                "MARPOL Annex I, OCIMF – для танкеров"
            ),
            (
                "03 Устройства, оборудование и снабжение",
                "(MMG) Руководство по проверке и техническому обслуживанию швартовного оборудования, включая тросы",
                "(MMG) Guidelines for inspection and maintenance of mooring equipment including lines",
                "Не подлежит рассмотрению",
                r"\\192.168.1.98\02 Library\00 Шаблоны\089.003 (MMG) Руководство ТОиПШО",
                ""
            ),
            (
                "03 Устройства, оборудование и снабжение",
                "(ETB) Буклет аварийной буксировки",
                "(ETB) Emergency towing booklet",
                "Не подлежит рассмотрению",
                r"\\192.168.1.98\02 Library\00 Шаблоны\089.004 (ETB) Буклет АБ",
                "Согласно SOLAS 74 Ch.II-1, Regulation 3-4 and relating MSC.1/Circ.1255"
            ),
            (
                "03 Устройства, оборудование и снабжение",
                "(IMDG) Перевозка опасных грузов",
                "(IMDG) Grounding of dangerous cargoes carriage by sea",
                "Подлежит рассмотрению",
                r"\\192.168.1.98\02 Library\00 Шаблоны\089.005 (IMDG) Перевозка ОГ",
                "Согласно SOLAS-74 Chapter II-2, Regulation 19"
            ),
            (
                "03 Устройства, оборудование и снабжение",
                "(DVP) Проект перегона",
                "(DVP) Delivery Voyage Plan",
                "Подлежит рассмотрению",
                r"\\192.168.1.98\02 Library\00 Шаблоны\089.006 (DVP) Проект перегона",
                ""
            ),
            (
                "03 Устройства, оборудование и снабжение",
                "(CSM) Наставление по креплению грузов",
                "(CSM) Cargo Securing Manual",
                "Подлежит рассмотрению",
                r"\\192.168.1.98\02 Library\00 Шаблоны\089.007 (CSM) Наставление НКГ",
                ""
            ),
            (
                "03 Устройства, оборудование и снабжение",
                "(DCP) План по борьбе за живучесть",
                "(DCP) Damage Control Plan ",
                "Подлежит рассмотрению",
                r"\\192.168.1.98\02 Library\00 Шаблоны\089.008 (DCP) План БЖ",
                "Согласно SOLAS-74, Chapter II-I, Regulation 19 and MSC.1/Circ.1245"
            ),
            # 06 ПРОТИВОПОЖАРНАЯ БЕЗОПАСНОСТЬ
            (
                "06 Противопожарная безопасность",
                "(FSOB) Буклет эксплуатационного характера по мерам пожарной безопасности",
                "(FSOB) Fire safety operation booklet",
                "Подлежит рассмотрению",
                r"\\192.168.1.98\02 Library\00 Шаблоны\089.021 (FSOB) Буклет ЭКПБ",
                "Согласно требований SOLAS-74, Chapter II-2, Regulation 14"
            ),
            (
                "06 Противопожарная безопасность",
                "(FSTM) Наставление по подготовке персонала по противопожарной безопасности",
                "(FSTM) Fire safety training manual",
                "Подлежит рассмотрению",
                r"\\192.168.1.98\02 Library\00 Шаблоны\089.022 (FSTM) Наставление ППБ",
                "Согласно требований SOLAS-74, Chapter II-2, Regulation 15"
            ),
            (
                "06 Противопожарная безопасность",
                "(FCP) План противопожарной защиты и спасательных средств",
                "(FCP) Fire and safety control plan",
                "Подлежит рассмотрению",
                r"\\192.168.1.98\02 Library\00 Шаблоны\089.023 (FCP) План ППЗ СС",
                "Согласно требований SOLAS-74, Chapter II-2, Regulation 15 Р.2.4"
            ),
            (
                "06 Противопожарная безопасность",
                "(FPMP) План Технического Обслуживания и Ремонта Противопожарных Средств",
                "(FPMP) Maintenance plan for fire protection systems and appliances",
                "Подлежит рассмотрению",
                r"\\192.168.1.98\02 Library\00 Шаблоны\089.024 (FPMP) План ТОиР ПС",
                "Согласно требований SOLAS-74, Chapter II-2, Regulation 14 operational readiness and maintenance"
            ),
            # 11 ПРЕДОТВРАЩЕНИЕ ЗАГРЯЗНЕНИЯ С СУДОВ
            (
                "11 Предотвращение загрязнения с судов",
                "(GMP) План управления ликвидацией мусора",
                "(GMP)Shipboard Garbage management plan",
                "Не подлежит рассмотрению",
                r"\\192.168.1.98\02 Library\00 Шаблоны\089.041 (GMP) План ЛМ",
                "Согласно MARPOL 73/78 Regulation 10 Annex V"
            ),
            (
                "11 Предотвращение загрязнения с судов",
                "(SOPEP) Судовой план чрезвычайных мер по борьбе с загрязнением нефтью",
                "(SOPEP) Shipboard oil pollution emergency plan",
                "Подлежит рассмотрению",
                r"\\192.168.1.98\02 Library\00 Шаблоны\089.042 (SOPEP) План ЧМН",
                "Согласно MARPOL 73/78 Regulation 37 Annex I MEPC.54(32), MEPC.86(44)"
            ),
            (
                "11 Предотвращение загрязнения с судов",
                "(SMPEP) Судовой план чрезвычайных мер по борьбе с загрязнением моря",
                "(SMPEP) Shipboard marine pollution emergency plan",
                "Подлежит рассмотрению",
                r"\\192.168.1.98\02 Library\00 Шаблоны\089.043 (SMPEP) План ЧММ",
                "Согласно MARPOL 73/78 Regulation 37 Annex I ИМО MEPC.54(32), MEPC.85(44) Для химовозов"
            ),
            (
                "11 Предотвращение загрязнения с судов",
                "(SEEMP) План Управления Энергоэффективностью Судна",
                "(SEEMP) Shipboard Energy Efficiency Management Plan",
                "Подлежит рассмотрению",
                r"\\192.168.1.98\02 Library\00 Шаблоны\089.044 (SEEMP) План ЭЭС",
                "Согласно MARPOL Annex VI, Regulation 26.1"
            ),
            (
                "11 Предотвращение загрязнения с судов",
                "(EEXI) Технический файл",
                "(EEXI) EEXI technical file",
                "Подлежит рассмотрению",
                r"\\192.168.1.98\02 Library\00 Шаблоны\089.045 (EEXI) Техфайл EEXI",
                "Согласно Regulation 23 of the Amendments adopted by IMO Resolution MEPC.328(76)"
            ),
            (
                "11 Предотвращение загрязнения с судов",
                "(BWMP) План Управления Балластными Водами (по стандарту В-1 / D-2)",
                "(BWMP) Ballast water management plan",
                "Подлежит рассмотрению",
                r"\\192.168.1.98\02 Library\00 Шаблоны\089.046 (BWMP) План ПУБВ",
                "Согласно Правил B-1 Международной конвенции по контролю и обработке судового водяного балласта, МЕРС.127(53) (Руководство)"
            ),
            (
                "11 Предотвращение загрязнения с судов",
                "(BMP) План по ведению контроля за обрастанием судна",
                "(BMP) Biofouling Management Plan",
                "Не подлежит рассмотрению",
                r"\\192.168.1.98\02 Library\00 Шаблоны\089.047 (BWP) План БО",
                "Согласно IMO Resolution MEPC.207(62)"
            ),
            (
                "11 Предотвращение загрязнения с судов",
                "(PWOM) Наставление по эксплуатации в полярных вод",
                "(PWOM) Polar waters operation manual",
                "Подлежит рассмотрению",
                r"\\192.168.1.98\02 Library\00 Шаблоны\089.048 (PWOM) Наставление ПВ",
                ""
            ),
            (
                "11 Предотвращение загрязнения с судов",
                "(ECE) Расчет автономности плавания по условиям экологической безопасности",
                "(ECE) Endurance Calculation (Environmental Safety)",
                "Подлежит рассмотрению",
                r"\\192.168.1.98\02 Library\00 Шаблоны\089.049 (ECE) Расчет ЭА",
                ""
            ),
            (
                "11 Предотвращение загрязнения с судов",
                "(SDIC) Расчет интенсивности сброса сточных вод",
                "(SDIC) Sewage Discharge Intensity Calculation",
                "Подлежит рассмотрению",
                r"\\192.168.1.98\02 Library\00 Шаблоны\089.050 (SDIC) Расчет РССВ",
                ""
            ),
            (
                "11 Предотвращение загрязнения с судов",
                "(SECP) Процедура контроля выбросов окислов серы SOx",
                "(SECP) Instruction sulphur emission (Sox) control",
                "Не подлежит рассмотрению",
                r"\\192.168.1.98\02 Library\00 Шаблоны\089.051 (SECP) Процедура SOx",
                ""
            ),
            # 16 СПАСАТЕЛЬНЫЕ СРЕДСТВА
            (
                "16 Спасательные средства",
                "(LSA-TMA) Наставление по оставлению судна и подготовке судового персонала по спасательным средствам",
                "(LSA-TMA) Training manual and on-board training AIDS",
                "Не подлежит рассмотрению",
                r"\\192.168.1.98\02 Library\00 Шаблоны\089.061 (LSA-TMA) Наставление ОСП СС",
                "Согласно требований SOLAS-74, Chapter III, Regulation 35"
            ),
            (
                "16 Спасательные средства",
                "(LSA-MI) Инструкции по техническому обслуживанию и ремонту спасательных средств на судне",
                "(LSA-MI) Instructions for on-board maintenance of life-saving appliances",
                "Не подлежит рассмотрению",
                r"\\192.168.1.98\02 Library\00 Шаблоны\089.062 (LSA-MI) Инструкция ТОиР СС",
                "Согласно требований SOLAS-74, Chapter III, Regulation 20 operational readiness, maintenance and inspections"
            ),
            (
                "16 Спасательные средства",
                "(RPW) План и процедуры по подъему людей с поверхности воды",
                "(RPW) Plan and procedures for recovery of persons from the water",
                "Не подлежит рассмотрению",
                r"\\192.168.1.98\02 Library\00 Шаблоны\089.063 (RPW) План ППЛВ",
                "Согласно требований SOLAS Chapter III regulation 17-1"
            ),
        ]
        repo = ProjTemplateRepository(session)
        for part_rules, name_ru, name_en, reviewed, path, desc in types_data:
            repo.create_proj_template(
                name_ru,
                part_rules=part_rules,
                name_en=name_en,
                reviewed=reviewed,
                path=path, description=desc
            )

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
