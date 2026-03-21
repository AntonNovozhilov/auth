from fastapi import APIRouter
from src.app.schemas import (
    LoginRequest,
    MessageResponse,
)

router = APIRouter()


@router.post("/login", summary="Авторизация пользователя")
def login(
    login_data: LoginRequest,
) -> MessageResponse:
    """Авторизация пользователя"""
    return MessageResponse(message="login endpoint")
