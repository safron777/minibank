from datetime import date, datetime
import email
from shlex import join
from fastapi import APIRouter, Depends,Request,Response, BackgroundTasks


from sqlalchemy import BIGINT, BigInteger, Result, select, Computed
from app.database import async_session_maker
from app.account.models import User_accounts
from app.account.dao import AccountsDAO
from app.users.dao import UsersDAO
from app.account.schemas import SAccounts, SAccounts_balance,SAccounts_interest_rate
from app.users.dependencies import get_current_user
from app.users.models import Users
from app.users.schemas import SUserAuth
from app.account.schemas import SAccounts
from jose import jwt
from app.config import settings
import random


router_account = APIRouter(
    prefix="/accounts",
    tags=["Cчета"]
)

@router_account.post("/account_add",status_code=201)
async def add_account(
    account: SAccounts_balance,
   # background_tasks: BackgroundTasks,
    user: Users = Depends(get_current_user),
):
    account = await AccountsDAO.add(
        # id= user.id,

       username_acc= user.email,
        accounts = str(''.join(['408018101100',(str(1000000 - random.randint(0, 9999)))])),
        balance=account.balance,
        #interest_rate=account.interest_rate,
        data_time = datetime.utcnow()
        )
    
    return account

@router_account.post("/account_interest_rate",status_code=201)
async def add_account(
    account: SAccounts_interest_rate,
   # background_tasks: BackgroundTasks,
    user: Users = Depends(get_current_user),
):
    
    account = await AccountsDAO.update(
         id= user.id,

       # username_acc= user.email,
       # accounts = str(''.join(['408018101100',(str(1000000 - random.randint(0, 9999)))])),
        #balance=SAccounts_balance.balance+(account.interest_rate/100)*(SAccounts_balance.balance),
        interest_rate=account.interest_rate,
        data_time = datetime.utcnow()
        )
    
    return account


@router_account.get("/")
async def get_accounts(
    #username_acc= user.email,
    user: Users= Depends (get_current_user)
):
     

     accounts = await AccountsDAO.find_by_email(User_accounts.username_acc==user.email)

     return accounts
    


