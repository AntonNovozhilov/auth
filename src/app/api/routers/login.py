from fastapi import APIRouter
from src.app.schemas import (
    LoginRequest,
    MessageResponse,
)
from src.app.services.login_service import auth_to_account_user

router = APIRouter()


@router.post("/login", summary="Авторизация пользователя")
def login(
    login_data: LoginRequest,
) -> MessageResponse:
    """Авторизация пользователя"""
    return auth_to_account_user(login_data)
