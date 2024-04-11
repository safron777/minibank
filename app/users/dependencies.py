

from datetime import datetime
from fastapi import Depends, HTTPException, Request, status
from jose import jwt, JWTError, ExpiredSignatureError
from app.users.dao import UsersDAO

from app.config import settings

from app.exceptions import (
    IncorrectTokenFormatException,
    TokenAbsentException,
    TokenExpiredException,
    UserIsNotPresentException,
)

def get_token (request: Request):
    token = request.cookies.get("user_access_token")
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return token



async def get_current_user( token:str = Depends(get_token)):
    try : 
        payload = jwt.decode(
         token, settings.SECRET_KEY, settings.ALGORITHM  
        )
    except ExpiredSignatureError:
       
        raise TokenExpiredException
    except JWTError:
        raise IncorrectTokenFormatException
    user_id: str = payload.get("sub")
    if not user_id:
        raise UserIsNotPresentException
    user = await UsersDAO.find_one_or_none(id=int(user_id))
    if not user:
        raise UserIsNotPresentException
    return user

     