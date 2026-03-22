from src.app.schemas import LoginRequest, MessageResponse


def auth_to_account_user(data: LoginRequest) -> MessageResponse:
    """Авторизация в аккаунт пользователя."""
    return MessageResponse(message="login endpoint")
