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

    t3 = Teacher(
        teacher_id=1,
        last_name="Иванов",
        first_name="Иван",
        phone="+79991234567",
        experience_years=5,
        hire_date=date(2020, 9, 1),
    )

    print("--- Проверка равенства (по ID) ---")
    print(f"t1 == t3 (одинаковый ID): {t1 == t3}")
    print(f"t1 == t2 (разные ID): {t1 == t2}")

    print("\n--- Проверка сравнения по стажу ---")
    print(f"У Петрова ({t2.experience_years} лет) стаж больше, чем у Иванова ({t1.experience_years} лет): {t2 > t1}")
    print(f"t1 < t2: {t1 < t2}")


if __name__ == "__main__":
    main()