from src.teacher import Teacher


def main():
    print("--- 1. Создание из CSV-строки (from_string) ---")
    csv_line = "1;Петров;Петр;Петрович;+79001112233;petrov@mail.ru;5;Старший преподаватель;2020-09-01"
    teacher1 = Teacher.from_string(csv_line)
    print(f"Преподаватель из строки: {teacher1.last_name} {teacher1.first_name}, Должность: {teacher1.position}")

    print("\n--- 2. Создание из JSON (from_json) ---")
    json_data = """{
        "teacher_id": 2,
        "last_name": "Сидорова",
        "first_name": "Анна",
        "middle_name": "Сергеевна",
        "phone": "89201234567",
        "email": "sidorova@yandex.ru",
        "experience_years": 12,
        "position": "Профессор",
        "hire_date": "2012-02-15"
    }"""
    teacher2 = Teacher.from_json(json_data)
    print(f"Преподаватель из JSON: {teacher2.last_name} {teacher2.first_name}, Стаж: {teacher2.experience_years} лет")


if __name__ == "__main__":
    main()