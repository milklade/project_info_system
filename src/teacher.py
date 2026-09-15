import re
from datetime import date
from typing import Callable, Optional, TypeVar

T = TypeVar("T")


class Teacher:
    """Класс преподавателя без дублирования кода валидации."""

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

    # --- Универсальный метод установки с валидацией (устраняет дублирование) ---

    def _set_validated_attr(
        self,
        attr_name: str,
        value: T,
        validator: Callable[[T], bool],
        error_msg: str,
        allow_none: bool = False,
    ) -> None:
        if allow_none and value is None:
            setattr(self, attr_name, value)
            return

        if not validator(value):
            raise ValueError(f"{error_msg}: {value}")

        setattr(self, attr_name, value)

    # --- Свойства (Properties) ---

    @property
    def teacher_id(self) -> int:
        return self.__teacher_id

    @teacher_id.setter
    def teacher_id(self, value: int) -> None:
        self._set_validated_attr(
            "_Teacher__teacher_id",
            value,
            self.validate_id,
            "Некорректный ID преподавателя",
        )

    @property
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self, value: str) -> None:
        self._set_validated_attr(
            "_Teacher__last_name",
            value,
            self.validate_name_part,
            "Некорректная фамилия",
        )

    @property
    def first_name(self) -> str:
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str) -> None:
        self._set_validated_attr(
            "_Teacher__first_name",
            value,
            self.validate_name_part,
            "Некорректное имя",
        )

    @property
    def middle_name(self) -> Optional[str]:
        return self.__middle_name

    @middle_name.setter
    def middle_name(self, value: Optional[str]) -> None:
        self._set_validated_attr(
            "_Teacher__middle_name",
            value,
            self.validate_name_part,
            "Некорректное отчество",
            allow_none=True,
        )

    @property
    def phone(self) -> str:
        return self.__phone

    @phone.setter
    def phone(self, value: str) -> None:
        self._set_validated_attr(
            "_Teacher__phone",
            value,
            self.validate_phone,
            "Некорректный номер телефона",
        )

    @property
    def email(self) -> Optional[str]:
        return self.__email

    @email.setter
    def email(self, value: Optional[str]) -> None:
        self._set_validated_attr(
            "_Teacher__email",
            value,
            self.validate_email,
            "Некорректный email",
            allow_none=True,
        )

    @property
    def experience_years(self) -> int:
        return self.__experience_years

    @experience_years.setter
    def experience_years(self, value: int) -> None:
        self._set_validated_attr(
            "_Teacher__experience_years",
            value,
            self.validate_experience,
            "Некорректный стаж работы",
        )

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
        self._set_validated_attr(
            "_Teacher__hire_date",
            value,
            self.validate_hire_date,
            "Некорректная дата найма",
        )