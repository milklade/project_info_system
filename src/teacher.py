from datetime import date
from typing import Optional


class Teacher:
    """Класс, представляющий преподавателя."""

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
        self.__teacher_id = teacher_id
        self.__last_name = last_name
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__phone = phone
        self.__email = email
        self.__experience_years = experience_years
        self.__position = position
        self.__hire_date = hire_date

    # --- Геттеры и Сеттеры ---

    @property
    def teacher_id(self) -> int:
        return self.__teacher_id

    @teacher_id.setter
    def teacher_id(self, value: int) -> None:
        self.__teacher_id = value

    @property
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self, value: str) -> None:
        self.__last_name = value

    @property
    def first_name(self) -> str:
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str) -> None:
        self.__first_name = value

    @property
    def middle_name(self) -> Optional[str]:
        return self.__middle_name

    @middle_name.setter
    def middle_name(self, value: Optional[str]) -> None:
        self.__middle_name = value

    @property
    def phone(self) -> str:
        return self.__phone

    @phone.setter
    def phone(self, value: str) -> None:
        self.__phone = value

    @property
    def email(self) -> Optional[str]:
        return self.__email

    @email.setter
    def email(self, value: Optional[str]) -> None:
        self.__email = value

    @property
    def experience_years(self) -> int:
        return self.__experience_years

    @experience_years.setter
    def experience_years(self, value: int) -> None:
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
        self.__hire_date = value