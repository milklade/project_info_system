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

    print("--- Чтение данных ---")
    print(f"ID: {teacher.teacher_id}")
    print(f"ФИО: {teacher.last_name} {teacher.first_name} {teacher.middle_name}")
    print(f"Телефон: {teacher.phone}")
    print(f"Email: {teacher.email}")

    print("\n--- Проверка сеттера ---")
    teacher.position = "Профессор"
    print(f"Новая должность: {teacher.position}")


if __name__ == "__main__":
    main()