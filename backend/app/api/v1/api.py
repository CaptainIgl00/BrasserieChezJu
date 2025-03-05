from fastapi import APIRouter
from app.api.v1.endpoints import menu, categories, dishes, wines

api_router = APIRouter()

api_router.include_router(menu.router, prefix="/menu", tags=["menu"])
api_router.include_router(categories.router, prefix="/categories", tags=["categories"])
api_router.include_router(dishes.router, prefix="/dishes", tags=["dishes"])
api_router.include_router(wines.router, prefix="/wines", tags=["wines"]) 