from pydantic import BaseModel, Field


class MessageResponse(BaseModel):
    """Схема для сообщений"""

    message: str = Field(example="success", description="Сообщение")
