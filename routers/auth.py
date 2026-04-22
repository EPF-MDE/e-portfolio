from fastapi import APIRouter, Request, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select

from core.database_2 import get_session
from schemas.User import User

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
def login(request: Request):
    return templates.TemplateResponse(request, "login.html", {"request": request})


@router.post("/login")
def login_user(
    mail: str = Form(...),
    password: str = Form(...),
    session: Session = Depends(get_session),
):
    # debug
    print("DEBUG LOGIN:")
    print("INPUT:", mail, password)

    user = session.exec(select(User).where(User.mail == mail)).first()

    print("USER:", user)

    if user:
        print("DB PASSWORD:", user.password)

    if not user or user.password != password:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    return RedirectResponse(f"/profil?mail={mail}", status_code=303)

@router.get("/logout")
def logout():
    return RedirectResponse("/", status_code=303)


