from fastapi import FastApi, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime

app = FastApi()

templates = Jinja2Templates(directory="templates")


class User(BaseModel):
    name: str
    age: int
    mail: str
    phone: str


class Experience(BaseModel):
    title: str
    date_start: datetime
    date_end: datetime
    description: str
    company: str
