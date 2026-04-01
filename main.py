from fastapi import FastApi
from pydantic import BaseModel

app = FastApi()


class User(BaseModel):
    name: str
    age: int
    mail: str
    phone: str
