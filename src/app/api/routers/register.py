from fastapi import APIRouter
from src.app.schemas import (
    RegisterRequest,
    MessageResponse,
)
from src.app.services.register_service import create_account_user


router = APIRouter()


@router.post(
    "/register",
    summary="Регистрация пользователя",
)
def register(
    register_data: RegisterRequest,
) -> MessageResponse:
    """Регистрация пользователя"""
    return create_account_user(register_data)
