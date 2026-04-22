from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.database_2 import create_db_and_tables

from routers import auth, user, experience

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# Routers
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(experience.router)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
