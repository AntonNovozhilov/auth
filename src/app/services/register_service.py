from src.app.schemas import RegisterRequest, MessageResponse

def create_account_user(data: RegisterRequest) -> MessageResponse:
    """Создаем аккаунт пользователя."""
    return MessageResponse(message="register endpoint")