import json
import re
from datetime import date
from typing import Any, Optional

from src.teacherShort import TeacherShort


class Teacher(TeacherShort):
    """Полный класс преподавателя (Дочерний класс от TeacherShort)."""

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
        # Вызов конструктора родительского класса TeacherShort
        # (убираем дублирование инициализации ID, ФИО и телефона)
        super().__init__(
            teacher_id=teacher_id,
            last_name=last_name,
            first_name=first_name,
            phone=phone,
            middle_name=middle_name,
        )

        # Инициализация дополнительных полей класса Teacher
        self.email = email
        self.experience_years = experience_years
        self.position = position
        self.hire_date = hire_date

    # --- Дополнительные статические методы валидации ---

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

    # --- Альтернативные конструкторы (@classmethod) ---

    @classmethod
    def from_string(cls, data_str: str, sep: str = ";") -> "Teacher":
        parts = [p.strip() for p in data_str.split(sep)]
        if len(parts) < 9:
            raise ValueError(f"Строка должна содержать 9 элементов через '{sep}'")

        return cls(
            teacher_id=int(parts[0]),
            last_name=parts[1],
            first_name=parts[2],
            middle_name=parts[3] if parts[3] else None,
            phone=parts[4],
            email=parts[5] if parts[5] else None,
            experience_years=int(parts[6]),
            position=parts[7] if parts[7] else None,
            hire_date=date.fromisoformat(parts[8]),
        )

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Teacher":
        hire_date_val = data.get("hire_date")
        if isinstance(hire_date_val, str):
            hire_date_val = date.fromisoformat(hire_date_val)

        return cls(
            teacher_id=int(data["teacher_id"]),
            last_name=data["last_name"],
            first_name=data["first_name"],
            middle_name=data.get("middle_name"),
            phone=data["phone"],
            email=data.get("email"),
            experience_years=int(data["experience_years"]),
            position=data.get("position"),
            hire_date=hire_date_val,
        )

    @classmethod
    def from_json(cls, json_str: str) -> "Teacher":
        data = json.loads(json_str)
        return cls.from_dict(data)

    # --- Свойства (Properties) для специфичных полей ---

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

    # --- Расчетные свойства ---

    @property
    def days_employed(self) -> int:
        return (date.today() - self.hire_date).days

    # --- Строковое представление ---

    def __repr__(self) -> str:
        return (
            f"Teacher(teacher_id={self.teacher_id!r}, "
            f"last_name={self.last_name!r}, "
            f"first_name={self.first_name!r}, "
            f"phone={self.phone!r}, "
            f"experience_years={self.experience_years!r}, "
            f"hire_date={self.hire_date!r})"
        )

    def __str__(self) -> str:
        pos = f", Должность: {self.position}" if self.position else ""
        return f"Преподаватель (полный): {self.full_name} (ID: {self.teacher_id}{pos})"

    # --- Сравнения по стажу ---

    def __lt__(self, other: "Teacher") -> bool:
        if not isinstance(other, Teacher):
            return NotImplemented
        return self.experience_years < other.experience_years

    def __le__(self, other: "Teacher") -> bool:
        if not isinstance(other, Teacher):
            return NotImplemented
        return self.experience_years <= other.experience_years

    def __gt__(self, other: "Teacher") -> bool:
        if not isinstance(other, Teacher):
            return NotImplemented
        return self.experience_years > other.experience_years

    def __ge__(self, other: "Teacher") -> bool:
        if not isinstance(other, Teacher):
            return NotImplemented
        return self.experience_years >= other.experience_years