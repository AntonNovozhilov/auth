from fastapi import APIRouter
from src.app.schemas import (
    RegisterRequest,
    MessageResponse,
)


router = APIRouter()


@router.post(
    "/register",
    summary="Регистрация пользователя",
)
def register(
    register_data: RegisterRequest,
) -> MessageResponse:
    """Регистрация пользователя"""
    return MessageResponse(message="register endpoint")
