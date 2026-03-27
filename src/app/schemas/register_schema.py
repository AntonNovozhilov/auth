from pydantic import BaseModel, Field, EmailStr, SecretStr, field_validator, ConfigDict
from datetime import date
from pydantic.types import StringConstraints
from typing import Annotated

NamePattern = Annotated[str, StringConstraints(min_length=2, max_length=50)]
NickNamePattern = Annotated[NamePattern, StringConstraints(min_length=4, max_length=50)]


class RegisterRequest(BaseModel):
    """Схема для регистрации пользователя"""

    first_name: NamePattern = Field(json_schema_extra={"example": "John"}, description="Имя")
    last_name: NamePattern = Field(json_schema_extra={"example": "Doe"}, description="Фамилия")
    email: EmailStr = Field(
        json_schema_extra={"example": "john.doe@example.com"},
        description="Email",
    )
    nickname: NickNamePattern = Field(
        json_schema_extra={"example": "johndoe"}, description="Никнейм"
    )
    birth_date: date = Field(
        json_schema_extra={"example": "2000-01-01"},
        description="Дата рождения",
    )
    password: SecretStr = Field(json_schema_extra={"example": "Password"}, description="Пароль")

    model_config = ConfigDict(
        extra="forbid",
    )

    @field_validator("password", mode="after")
    def validate_password(cls, v: SecretStr) -> SecretStr:
        if len(v) < 8:
            raise ValueError("Пароль не должен быть короче 8 символов")
        return v
