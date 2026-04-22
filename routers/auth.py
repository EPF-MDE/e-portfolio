from fastapi import APIRouter, Request, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select

from core.database_2 import get_session
from schemas.User import User

router = APIRouter()
templates = Jinja2Templates(directory="templates")


# Page login (root)
@router.get("/", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse(request, "login.html", {"request": request})


# Page login (optionnel mais utile)
@router.get("/login", response_class=HTMLResponse)
def login_page_alias(request: Request):
    return templates.TemplateResponse(request, "login.html", {"request": request})


# Login POST
@router.post("/login")
def login_user(
    mail: str = Form(...),
    password: str = Form(...),
    session: Session = Depends(get_session),
):
    user = session.exec(select(User).where(User.mail == mail)).first()

    if not user or user.password != password:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    return RedirectResponse(f"/profil?mail={mail}", status_code=303)


# Logout
@router.get("/logout")
def logout():
    return RedirectResponse("/", status_code=303)
