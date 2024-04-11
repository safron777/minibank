from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi import templating
from app import pages

from app.account.router import account_add, get_accounts
from app.users.dependencies import get_current_user
from app.users.router import register_user


router = APIRouter(
    prefix= "/pages",
    tags= ["Frontend"]
)

templates = Jinja2Templates(directory="app/templates")

@router.get("/login", response_class=HTMLResponse)
async def get_login_page(request: Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})


@router.get("/register", response_class=HTMLResponse)
async def get_register_page(request: Request):
   return templates.TemplateResponse("auth/register.html", {"request": request})




@router.get("/account", response_class=HTMLResponse)
async def get_accounts_page(
    request: Request,
    accounts=Depends(get_accounts),
    users= Depends(get_current_user)
    
):
    
    
    return templates.TemplateResponse(
        name="account/account.html", 
        context={"request": request, "users":users,"account": accounts})


@router.get("/add-account", response_class=HTMLResponse)
async def get_add_accounts(
    request: Request,
    users= Depends(get_current_user)):
   return templates.TemplateResponse("account/add-account.html", {"request": request, "users":users})


"""""        
@router.post("/add-account",response_class=HTMLResponse)
#@router.get("/add_account",response_class=HTMLResponse)
async def add_account(
    request: Request,
    users = Depends(get_current_user),
    account = Depends (account_add)
    
):
    #print(account)
    return templates.TemplateResponse(
      name="account/add-account.html",
      context={"request":request, "users":users,"account":account})
    
"""    