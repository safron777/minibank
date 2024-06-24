from app.database import async_session_maker
from app.feature_toggle.models import Feature_toggle
from app.database import async_session_maker
from sqlalchemy import select


class FTDAO:
   
    @classmethod
    async def find_all(cls):
        async with async_session_maker() as session:
            query=select (Feature_toggle)
            ft = await session.execute(query)
            return ft.scalars().all()