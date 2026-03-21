from pydantic import BaseModel, Field


class RegisterRequest(BaseModel):
    """Схема для регистрации пользователя"""

    first_name: str = Field(example="John", description="Имя")
    last_name: str = Field(example="Doe", description="Фамилия")
    email: str = Field(
        example="john.doe@example.com",
        description="Email",
    )
    nickname: str = Field(example="johndoe", description="Никнейм")
    birth_date: str = Field(
        example="2000-01-01",
        description="Дата рождения",
    )
    password: str = Field(example="Password", description="Пароль")
