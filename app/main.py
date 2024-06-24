import time

from argparse import OPTIONAL
from fastapi import FastAPI, Request, Query, Depends
from typing import Optional
from pydantic import BaseModel


from app.account.router import router_account as router_account
from app.users.router import router_auth as router_auth
from app.feature_toggle.router import router as router_ft

from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.logger import logger

from app.pages.router import router as router_pages

app=FastAPI(
    title="Minibank",
    version="0.1.0",
    root_path="/api",
)

app.mount("/static", StaticFiles(directory="app/static"), "static")
#app.include_router (router_users)
app.include_router (router_auth)
app.include_router (router_account)
app.include_router (router_ft)


# Подключение CORS,
origins = [
    # 8000 - порт
    "http://127.0.0.1:8000",
    "http://127.0.0.1:443"
    ,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", 
                   "Access-Control-Allow-Origin",
                   "Authorization"],
)

app.include_router (router_pages)

app.mount("/static", StaticFiles(directory="app/static"), "static")


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    # При подключении Prometheus + Grafana подобный лог не требуется
    logger.info("Request handling time", extra={
        "process_time": round(process_time, 4)
    })
    return response