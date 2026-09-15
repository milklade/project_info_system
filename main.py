from src.teacherShort import TeacherShort


def main():
    print("--- Пункт 8: Создание краткой версии объекта (TeacherShort) ---")
    ts = TeacherShort(
        teacher_id=1,
        last_name="Иванов",
        first_name="Иван",
        middle_name="Иванович",
        phone="+79991234567",
    )

    print(f"Вывод __str__: {ts}")
    print(f"Вывод __repr__: {ts!r}")
    print(f"ФИО: {ts.full_name}")


if __name__ == "__main__":
    main()