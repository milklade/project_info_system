from datetime import date
from src.teacher import Teacher
from src.teacherShort import TeacherShort


def main():
    print("--- Пункт 9: Проверка иерархии наследования (Teacher -> TeacherShort) ---")

    # 1. Создаем объект дочернего класса Teacher
    t = Teacher(
        teacher_id=1,
        last_name="Иванов",
        first_name="Иван",
        middle_name="Иванович",
        phone="+79991234567",
        email="ivanov@vuz.ru",
        experience_years=10,
        position="Доцент",
        hire_date=date(2020, 9, 1),
    )

    # 2. Проверяем наследование через isinstance
    print(f"Объект 't' является экземпляром Teacher: {isinstance(t, Teacher)}")
    print(f"Объект 't' является экземпляром TeacherShort: {isinstance(t, TeacherShort)}")

    # 3. Доступ к методам и свойствам родительского и дочернего классов
    print(f"ФИО (из TeacherShort): {t.full_name}")
    print(f"Дней работает (из Teacher): {t.days_employed}")
    print(f"Вывод __str__: {t}")


if __name__ == "__main__":
    main()