import re
from datetime import date
from typing import Optional


class Teacher:
    """Класс, представляющий преподавателя с валидацией полей."""

    def __init__(
        self,
        teacher_id: int,
        last_name: str,
        first_name: str,
        phone: str,
        experience_years: int,
        hire_date: date,
        middle_name: Optional[str] = None,
        email: Optional[str] = None,
        position: Optional[str] = None,
    ):
        self.teacher_id = teacher_id
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.phone = phone
        self.email = email
        self.experience_years = experience_years
        self.position = position
        self.hire_date = hire_date

    # --- Статические методы валидации ---

    @staticmethod
    def validate_id(val: int) -> bool:
        return isinstance(val, int) and val > 0

    @staticmethod
    def validate_name_part(val: str) -> bool:
        pattern = r"^[А-ЯЁ][а-яё]+(-[А-ЯЁ][а-яё]+)?$"
        return isinstance(val, str) and bool(re.match(pattern, val))

    @staticmethod
    def validate_phone(val: str) -> bool:
        pattern = r"^(\+7|8)\d{10}$"
        return isinstance(val, str) and bool(re.match(pattern, val))

    @staticmethod
    def validate_email(val: str) -> bool:
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return isinstance(val, str) and bool(re.match(pattern, val))

    @staticmethod
    def validate_experience(val: int) -> bool:
        return isinstance(val, int) and val >= 0

    @staticmethod
    def validate_hire_date(val: date) -> bool:
        return isinstance(val, date) and val <= date.today()

    # --- Геттеры и Сеттеры с вызовом валидации ---

    @property
    def teacher_id(self) -> int:
        return self.__teacher_id

    @teacher_id.setter
    def teacher_id(self, value: int) -> None:
        if not self.validate_id(value):
            raise ValueError(f"Некорректный ID преподавателя: {value}")
        self.__teacher_id = value

    @property
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self, value: str) -> None:
        if not self.validate_name_part(value):
            raise ValueError(f"Некорректная фамилия: {value}")
        self.__last_name = value

    @property
    def first_name(self) -> str:
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str) -> None:
        if not self.validate_name_part(value):
            raise ValueError(f"Некорректное имя: {value}")
        self.__first_name = value

    @property
    def middle_name(self) -> Optional[str]:
        return self.__middle_name

    @middle_name.setter
    def middle_name(self, value: Optional[str]) -> None:
        if value is not None and not self.validate_name_part(value):
            raise ValueError(f"Некорректное отчество: {value}")
        self.__middle_name = value

    @property
    def phone(self) -> str:
        return self.__phone

    @phone.setter
    def phone(self, value: str) -> None:
        if not self.validate_phone(value):
            raise ValueError(f"Некорректный номер телефона: {value}")
        self.__phone = value

    @property
    def email(self) -> Optional[str]:
        return self.__email

    @email.setter
    def email(self, value: Optional[str]) -> None:
        if value is not None and not self.validate_email(value):
            raise ValueError(f"Некорректный email: {value}")
        self.__email = value

    @property
    def experience_years(self) -> int:
        return self.__experience_years

    @experience_years.setter
    def experience_years(self, value: int) -> None:
        if not self.validate_experience(value):
            raise ValueError(f"Некорректный стаж работы: {value}")
        self.__experience_years = value

    @property
    def position(self) -> Optional[str]:
        return self.__position

    @position.setter
    def position(self, value: Optional[str]) -> None:
        self.__position = value

    @property
    def hire_date(self) -> date:
        return self.__hire_date

    @hire_date.setter
    def hire_date(self, value: date) -> None:
        if not self.validate_hire_date(value):
            raise ValueError(f"Некорректная дата найма: {value}")
        self.__hire_date = value