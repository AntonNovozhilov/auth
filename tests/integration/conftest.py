from fastapi.testclient import TestClient
from src.app.main import create_app
from pytest import fixture


@fixture
def test_app() -> TestClient:
    """Тестовый клиент для тестирования эндпоинтов"""
    return TestClient(create_app())
