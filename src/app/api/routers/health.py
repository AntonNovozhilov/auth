from fastapi import APIRouter

router = APIRouter()


@router.get("/health", summary="Технический эндпоинт")
def health():
    return {"status": "ok"}
