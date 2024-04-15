from datetime import date, datetime
import email
from re import I
from shlex import join
import math

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
from sqlalchemy import select, insert, update
from app.database import async_session_maker


router_account = APIRouter(
    prefix="/accounts",
    tags=["Cчета"]
)

@router_account.post("/account_add",status_code=201)
async def account_add(
    account: SAccounts_balance,
   # background_tasks: BackgroundTasks,
    user: Users = Depends(get_current_user),
):
    account = await AccountsDAO.add(
        # id= user.id,

       username_acc = user.email,
        accounts = str(''.join(['408018101100',(str(1000000 - random.randint(0, 9999)))])),
        balance=account.balance,
        interest_rate=account.interest_rate,
        data_time = datetime.utcnow()
        )
    
    return account

@router_account.get("/account_increase_balance",status_code=201)
async def update(
    increase_balance: float,
    account_one: str,
    user: Users = Depends(get_current_user)
):
    
    acc1 = await AccountsDAO.find_one_or_none (accounts = account_one)
    
    account = tuple()
    account= acc1
    acc_delete = await AccountsDAO.delete (id = account.id)
    #print (acc_delete)
    
    account1=await AccountsDAO.add(
        id=,
        username_acc = user.email,
        accounts = account_one,
        balance=account.balance+increase_balance,
        interest_rate=account.interest_rate,
        data_time = datetime.utcnow()
         
    )
    
    return account1
    



@router_account.get("/all_accounts")
async def get_accounts(
    #username_acc= user.email,
    user: Users= Depends (get_current_user)
):
     

     accounts = await AccountsDAO.find_by_email(User_accounts.username_acc==user.email)

     return accounts
    

