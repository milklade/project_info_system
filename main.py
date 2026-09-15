from datetime import date
from src.teacher import Teacher


def main():
    t1 = Teacher(
        teacher_id=1,
        last_name="Иванов",
        first_name="Иван",
        phone="+79991234567",
        experience_years=5,
        hire_date=date(2020, 9, 1),
    )

    t2 = Teacher(
        teacher_id=2,
        last_name="Петров",
        first_name="Петр",
        phone="+79001112233",
        experience_years=12,
        hire_date=date(2013, 9, 1),
    )

    # Объект с таким же ID, как у t1 (дубликат по бизнес-логике)
    t1_duplicate = Teacher(
        teacher_id=1,
        last_name="Иванов",
        first_name="Иван",
        phone="+79991234567",
        experience_years=5,
        hire_date=date(2020, 9, 1),
    )

    print("--- 1. Использование объектов в множестве (set) ---")
    teachers_set = {t1, t2, t1_duplicate}
    print(f"Размер множества (должен быть 2, так как t1 и t1_duplicate совпали): {len(teachers_set)}")

    print("\n--- 2. Использование объектов в качестве ключей словаря (dict) ---")
    workloads = {
        t1: "120 часов",
        t2: "180 часов",
    }
    print(f"Нагрузка преподавателя t1_duplicate (поиск по хэшу ID): {workloads.get(t1_duplicate)}")


if __name__ == "__main__":
    main()