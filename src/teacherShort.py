import re
from typing import Any, Callable, Optional, TypeVar

T = TypeVar("T")


class TeacherShort:
    """Краткая версия сущности преподавателя."""

    def __init__(
        self,
        teacher_id: int,
        last_name: str,
        first_name: str,
        phone: str,
        middle_name: Optional[str] = None,
    ):
        self.teacher_id = teacher_id
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.phone = phone

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

    # --- Вспомогательный метод валидации ---

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
            "_TeacherShort__teacher_id",
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
            "_TeacherShort__last_name",
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
            "_TeacherShort__first_name",
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
            "_TeacherShort__middle_name",
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
            "_TeacherShort__phone",
            value,
            self.validate_phone,
            "Некорректный номер телефона",
        )

    # --- Расчетные свойства ---

    @property
    def full_name(self) -> str:
        """Возвращает полное ФИО преподавателя."""
        if self.middle_name:
            return f"{self.last_name} {self.first_name} {self.middle_name}"
        return f"{self.last_name} {self.first_name}"

    # --- Строковое представление ---

    def __repr__(self) -> str:
        return (
            f"TeacherShort(teacher_id={self.teacher_id!r}, "
            f"full_name={self.full_name!r}, phone={self.phone!r})"
        )

    def __str__(self) -> str:
        return f"Преподаватель (кратко): {self.full_name} | Тел: {self.phone} (ID: {self.teacher_id})"

    # --- Сравнение на равенство и хэширование ---

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TeacherShort):
            return NotImplemented
        return self.teacher_id == other.teacher_id

    def __hash__(self) -> int:
        return hash(self.teacher_id)