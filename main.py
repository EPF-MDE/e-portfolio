from fastapi import FastAPI, Request, Form, status, HTTPException, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from typing import Annotated
from datetime import datetime
from sqlmodel import Session
from fastapi.staticfiles import StaticFiles


from core.database_2 import create_db_and_tables, get_session
from schemas.User import User
from schemas.Experiences import Experience
from schemas.Education import Education


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


user1 = User(name="Alice", age=25, mail="alice@email.com", phone="0600000000")
# get_session.add(user1)
# get_session.commit()
# get_session.refresh(user1)

Education1 = Education(
    school_name="University of Example",
    date_start=datetime(2015, 9, 1),
    date_end=datetime(2019, 6, 30),
    description="Bachelor's degree in Computer Science",
    major="Computer Science",
)
experience_list = []
experience1 = Experience(
    title="Software Engineer",
    date_start=datetime(2019, 7, 1),
    date_end=datetime(2021, 12, 31),
    description="Worked on developing web applications using Python and JavaScript.",
    company="Tech Company",
)
experience_list.append(experience1)


@app.get("/", response_class=HTMLResponse)
def connexion(request: Request):
    return templates.TemplateResponse(
        request,
        name="login.html",
        context={
            "name": user1.name,
            "age": user1.age,
            "mail": user1.mail,
            "phone": user1.phone,
            "experiences": experience_list,
        },
    )


@app.get("/create_user", response_class=HTMLResponse)
def show_creating_user_form(request: Request):
    return templates.TemplateResponse(
        request, name="create_user.html", context={"request": request}
    )


@app.post("/create_user", response_class=HTMLResponse)
def create_exp(
    name: Annotated[str, Form()],
    age: Annotated[int, Form()],
    mail: Annotated[str, Form()],
    phone: Annotated[str, Form()],
    session: Session = Depends(get_session),
):

    user = User(name=name, age=age, mail=mail, phone=phone)

    # sauvegarde en base
    session.add(user)
    session.commit()
    session.refresh(user)

    return RedirectResponse("/", status_code=303)


@app.get("/profil", response_class=HTMLResponse)
def show_user(request: Request):
    return templates.TemplateResponse(
        request,
        name="profil.html",
        context={
            "name": user1.name,
            "age": user1.age,
            "mail": user1.mail,
            "phone": user1.phone,
            "experiences": experience_list,
        },
    )


@app.get("/profil/experience", response_class=HTMLResponse)
def show_experience_form(request: Request):
    return templates.TemplateResponse(
        request, name="experience.html", context={"request": request}
    )


@app.post("/profil/experience", response_class=HTMLResponse)
def create_exp(
    title: Annotated[str, Form()],
    date_start: Annotated[str, Form()],
    date_end: Annotated[str, Form()],
    description: Annotated[str, Form()],
    company: Annotated[str, Form()],
    session: Session = Depends(get_session),
):
    # Convertir les dates de string à datetime si nécessaire
    date_start_dt = datetime.strptime(date_start, "%Y-%m-%d")
    date_end_dt = datetime.strptime(date_end, "%Y-%m-%d")

    experience = Experience(
        title=title,
        date_start=date_start_dt,
        date_end=date_end_dt,
        description=description,
        company=company,
    )

    # sauvegarde en base
    session.add(experience)
    session.commit()
    session.refresh(experience)

    return RedirectResponse("/profil", status_code=303)
