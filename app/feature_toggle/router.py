from fastapi import APIRouter
from sqlalchemy import select
from app.database import async_session_maker
from app.feature_toggle.models import Feature_toggle
from app.feature_toggle.dao import FTDAO

router = APIRouter(
    prefix="/feature_toggle",
    tags=["Тоглы"]
)

@router.get ("")
async def get_feature_toggle():
    return await FTDAO.find_all()