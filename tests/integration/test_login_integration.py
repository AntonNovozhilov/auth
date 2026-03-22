from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fastapi.testclient import TestClient
from src.app.schemas import LoginRequest, MessageResponse


def test_login_integration(test_app: "TestClient") -> None:
    """Тест для эндпоинта /login"""
    data = LoginRequest(login="test", password="Password1")
    request = test_app.post("/login", json=data.model_dump())
    assert request.status_code == 200
    assert request.json() == MessageResponse(message="login endpoint").model_dump()
