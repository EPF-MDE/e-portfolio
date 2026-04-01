from fastapi import FastApi, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastApi()

templates = Jinja2Templates(directory="templates")


class User(BaseModel):
    name: str
    age: int
    mail: str
    phone: str
