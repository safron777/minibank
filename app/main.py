from argparse import OPTIONAL
from fastapi import FastAPI, requests, Query, Depends
from typing import Optional
from pydantic import BaseModel
from app.account.router import router_account as router_account
from app.users.router import router_auth as router_auth
from app.feature_toggle.router import router as router_ft


app=FastAPI()
#app.include_router (router_users)
app.include_router (router_auth)
app.include_router (router_account)
app.include_router (router_ft)





