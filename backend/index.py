from fastapi import FastAPI
from starlette.requests import Request
from fastapi.staticfiles import StaticFiles
from starlette.routing import request_response
from starlette.templating import Jinja2Templates
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from typing import List
import os

app = FastAPI(
    title='FastAPI Base',
    description='詳細説明を書くところ',
    version='1.0 beta'
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.mount("/static", StaticFiles(directory="./dist/static"), name="static")
templates = Jinja2Templates(directory="./dist")
jinja_env = templates.env

def index(request: Request):
    """
    WebUI表示
    """
    return templates.TemplateResponse('index.html', {'request': request})



