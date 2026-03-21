from fastapi import FastAPI
from src.app.api.routers.health import router as health_router

def create_app() -> FastAPI:
    """Создает приложение"""
    app = FastAPI(
        title="Сервис для регистрации и авторизации пользователей",
        description="Сервис на FastAPI для регистрации и авторизации пользователей",
        version="1.0.0",
    )
    app.include_router(health_router)
    return app

app = create_app()



