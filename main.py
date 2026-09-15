from datetime import date
from src.teacher import Teacher


def main():
    print("--- 1. Создание объекта с корректными данными ---")
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
    print(f"Преподаватель успешно создан: {teacher.last_name} {teacher.first_name}")

    print("\n--- 2. Перехват ошибки при попытке создать невалидный объект ---")
    try:
        invalid_teacher = Teacher(
            teacher_id=-1,  # Ошибка: отрицательный ID
            last_name="иванов",  # Ошибка: с маленькой буквы
            first_name="Иван",
            phone="12345",  # Ошибка: неверный формат телефона
            experience_years=-5,  # Ошибка: отрицательный стаж
            hire_date=date(2015, 9, 1),
        )
    except ValueError as e:
        print(f"Поймана ошибка валидации: {e}")


if __name__ == "__main__":
    main()