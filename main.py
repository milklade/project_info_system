from datetime import date
from src.teacher import Teacher


def main():
    teacher = Teacher(
        teacher_id=1,
        last_name="Иванов",
        first_name="Иван",
        middle_name="Иванович",
        phone="+79991234567",
        email="ivanov@example.com",
        experience_years=10,
        position="Доцент",
        hire_date=date(2015, 9, 1),
    )

    print("--- Проверка __str__ (пользовательский вид) ---")
    print(teacher)

    print("\n--- Проверка __repr__ (вид для разработчика) ---")
    print(repr(teacher))


if __name__ == "__main__":
    main()