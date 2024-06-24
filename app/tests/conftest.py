import asyncio
import json

from datetime import datetime
from app.main import app as fastapi_app
import pytest
from httpx import AsyncClient
from sqlalchemy import insert

from app.config import settings
from app.database import Base, async_session_maker, engine

from app.account.models import User_accounts
from app.users.models import Users
#from app.feature_toggle.models import Feature_toggle



@pytest.fixture(scope="session",autouse=True)
async def prepare_database():
    assert settings.MODE == "TEST"

    async with engine.begin as conn:
       await conn.run_sync(Base.metadata.drop_all)
       await conn.run_sync(Base.metadata.create_all)

    def open_mock_json(model:str):
        with open(f"app/tests/mock_{model}.json","r") as file:
            return json.load(file)
        
    
    
    users = open_mock_json("users")
    user_accounts= open_mock_json("user_accounts")
    #feature_toggle = open_mock_json("feature_toggle")

    

    async with async_session_maker() as session:
        for Model, values in [
            (Users, users),
            (User_accounts, user_accounts),
            #(Feature_toggle, feature_toggle),
            
        ]:
            query = insert(Model).values(values)
            await session.execute(query)

            await session.commit()
        
# Взято из документации к pytest-asyncio
# Создаем новый event loop для прогона тестов


@pytest.fixture(scope="session")
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
async def ac():
    "Асинхронный клиент для тестирования эндпоинтов"
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        yield ac


@pytest.fixture(scope="session")
async def authenticated_ac():
    "Асинхронный аутентифицированный клиент для тестирования эндпоинтов"
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        await ac.post("/api/auth/login", json={
            "email": "test@test.com",
            "password": "test",
        })
        assert ac.cookies["access_token"]
        yield ac
