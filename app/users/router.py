from fastapi import APIRouter, HTTPException, status, Response
from sqlalchemy import select

from typing import TYPE_CHECKING
"""""
if TYPE_CHECKING:
    # Убирает предупреждения отсутствия импорта и неприятные подчеркивания в 
    # PyCharm и VSCode
    
    from users.dao import UsersDAO
    from users.models import Users
    from users.schemas import SUserAuth, SUsers
"""""
from app.users.dao import UsersDAO
from app.users.models import Users
from app.users.schemas import SUserAuth, SUsers


from app.users.auth import get_password_hash, verify_password, authenticate_user,create_access_token



router_auth = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)
"""""
router_users = APIRouter(
    prefix="/users",
    tags=["Пользователи"],
)
"""""
@router_auth.post("/register")
async def register_user(user_data: SUsers):
     existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
     if existing_user:
          raise HTTPException (status_code=500)
     
     hashed_password = get_password_hash(user_data.password)
     await UsersDAO.add( email=user_data.email, password=hashed_password,lastname=user_data.lastname, firstname=user_data.firstname, surname=user_data.surname) 


@router_auth.post("/login")
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("user_access_token", access_token, httponly=True)
    return {"access_token": access_token}
     

@router_auth.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("users_access_token")
  



#@router.get ("")
#async def get_users():
#     async with async_session_maker() as session:
 #        query = select()
  #       result = await session.execute(query)
   #      return result.scalars().all()