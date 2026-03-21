from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    """Схема для авторизации пользователя"""

    login: str = Field(example="johndoe", description="Логин")
    password: str = Field(example="Password", description="Пароль")
