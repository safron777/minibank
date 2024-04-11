from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.account.models import User_accounts



class AccountsDAO (BaseDAO):
   model = User_accounts
   

