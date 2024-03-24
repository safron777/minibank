
from sqlalchemy import select, insert
from app.database import async_session_maker



class BaseDAO:
    model = None
    
    @classmethod
    async def find_by_id(cls,model_id: int):
         async with async_session_maker() as session:
            query=select (cls.model.__table__.columns).filter(id = model_id)
            result = await session.execute(query)
            return result.scalars_one_or_none()


    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().one_or_none()


    @classmethod
    async def find_all(cls,**filter_by):
        async with async_session_maker() as session:
            query=select (cls.model.__table__.columns).filter(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()


    @classmethod
    async def add(cls,**data):
         async with async_session_maker() as session:
            query=insert (cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def find_by_email(cls, email:str):
        async with async_session_maker() as session:
            query=select (cls.model.__table__.columns).filter(email)
            result = await session.execute(query)
            return result.mappings().all()

        
        


    
