# UML-диаграмма классов: TeacherShort / Teacher

```plantuml
@startuml

skinparam classAttributeIconSize 0

class TeacherShort {
    -teacher_id: int
    -last_name: string
    -first_name: string
    -middle_name: string
    -phone: string
    --
    +__init__(teacher_id, last_name, first_name, phone, middle_name)
    +full_name() : string
    {static} +validate_id(val: int) : bool
    {static} +validate_name_part(val: string) : bool
    {static} +validate_phone(val: string) : bool
    #_set_validated_attr(attr_name, value, validator, error_msg, allow_none)
    +__repr__() : string
    +__str__() : string
    +__eq__(other) : bool
    +__hash__() : int
}

class Teacher {
    -email: string
    -experience_years: int
    -position: string
    -hire_date: date
    --
    +__init__(teacher_id, last_name, first_name, phone, experience_years, hire_date, middle_name, email, position)
    {static} +from_string(data_str: string, sep: string) : Teacher
    {static} +from_dict(data: dict) : Teacher
    {static} +from_json(json_str: string) : Teacher
    {static} +validate_email(val: string) : bool
    {static} +validate_experience(val: int) : bool
    {static} +validate_hire_date(val: date) : bool
    +days_employed() : int
    +__repr__() : string
    +__str__() : string
    +__lt__(other: Teacher) : bool
    +__le__(other: Teacher) : bool
    +__gt__(other: Teacher) : bool
    +__ge__(other: Teacher) : bool
}

Teacher --|> TeacherShort : inherits / extends

@enduml
```

## Пояснения к обозначениям

- `-` — приватное поле (private)
- `+` — публичный метод (public)
- `#` — защищённый метод (protected)
- `{static}` — статический метод (`@staticmethod`)
- `Тип возврата` указывается через двоеточие после сигнатуры метода
- `--` — разделитель между разделом полей и разделом методов внутри блока класса
- `Teacher --|> TeacherShort` — сплошная линия с треугольной стрелкой — отношение наследования (`extends`) в PlantUML
