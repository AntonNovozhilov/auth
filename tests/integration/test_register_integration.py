from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fastapi.testclient import TestClient
from src.app.schemas import RegisterRequest, MessageResponse


def test_register_integration(test_app: "TestClient"):
    """Тест для эндпоинта /register"""
    data = RegisterRequest(
        first_name="Bao",
        last_name="Mao",
        email="Baomao@yandex.ru",
        nickname="Baomao",
        birth_date="2020-01-01",
        password="Password1",
    )
    request = test_app.post("/register", json=data.model_dump())
    assert request.status_code == 200
    assert request.json() == MessageResponse(message="register endpoint").model_dump()
