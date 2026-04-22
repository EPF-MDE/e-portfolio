from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select

from core.database_2 import get_session
from schemas.User import User
from schemas.Experiences import Experience

router = APIRouter()
templates = Jinja2Templates(directory="templates")


#Afficher le formulaire de création
@router.get("/create_user", response_class=HTMLResponse)
def show_form(request: Request):
    return templates.TemplateResponse(
        request,
        "create_user.html",
        {"request": request}
    )


#Créer un utilisateur
@router.post("/create_user")
def create_user(
    name: str = Form(...),
    age: int = Form(...),
    mail: str = Form(...),
    phone: str = Form(...),
    password: str = Form(...),
    session: Session = Depends(get_session),
):
    user = User(
        name=name,
        age=age,
        mail=mail,
        phone=phone,
        password=password
    )

    session.add(user)
    session.commit()
    session.refresh(user)

    return RedirectResponse("/", status_code=303)


#Page profil (avec données DB)
@router.get("/profil", response_class=HTMLResponse)
def show_profile(request: Request, session: Session = Depends(get_session)):

    user = session.exec(select(User)).first()
    experiences = session.exec(select(Experience)).all()

    return templates.TemplateResponse(
        request,
        "profil.html",
        {
            "request": request,
            "name": user.name if user else "",
            "age": user.age if user else "",
            "mail": user.mail if user else "",
            "phone": user.phone if user else "",
            "experiences": experiences,
        }
    )