from fastapi import FastAPI
from src.app.api.routers.health import (
    router as health_router,
)
from src.app.api.routers.register import (
    router as register_router,
)
from src.app.api.routers.login import (
    router as login_router,
)


def create_app() -> FastAPI:
    """Создает приложение."""
    app = FastAPI(
        title="Сервис для регистрации и авторизации пользователей",
        description="Сервис на FastAPI для регистрации и авторизации пользователей",
        version="1.0.0",
    )
    routers = [
        health_router,
        register_router,
        login_router,
    ]
    for router in routers:
        app.include_router(router)
    return app


app = create_app()
