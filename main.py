from fastapi import FastAPI, Request, Form, status, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from typing import Annotated
from datetime import datetime


from Models.User import User
from Models.Experiences import Experience
from Models.Education import Education


app = FastAPI()

templates = Jinja2Templates(directory="template")


user1 = User(
    name="Alice",
    age=25,
    mail="alice@email.com",
    phone="0600000000"
)
Education1 = Education(
    school_name="University of Example",
    date_start=datetime(2015, 9, 1),
    date_end=datetime(2019, 6, 30),
    description="Bachelor's degree in Computer Science",
    major="Computer Science"
)
experience_list = []
experience1 = Experience(
    title="Software Engineer",
    date_start=datetime(2019, 7, 1),
    date_end=datetime(2021, 12, 31),
    description="Worked on developing web applications using Python and JavaScript.",
    company="Tech Company"
)
experience_list.append(experience1)

@app.get("/profil", response_class=HTMLResponse)
def show_user(request: Request):
    return templates.TemplateResponse(
        request,
        name="profil.html",
        context={"name": user1.name, "age": user1.age, "mail": user1.mail, "phone": user1.phone, "experiences": experience_list}
    )

@app.get("/profil/experience", response_class=HTMLResponse)
def show_experience_form(request: Request):
    return templates.TemplateResponse(
        request,
        name="experience.html",
        context={"request": request}
    )


@app.post("/profil/experience", response_class=HTMLResponse)
def create_exp(
    title: Annotated[str, Form()],
    date_start: Annotated[str, Form()],
    date_end: Annotated[str, Form()],
    description: Annotated[str, Form()],
    company: Annotated[str, Form()]
):
    # Convertir les dates de string à datetime si nécessaire
    date_start_dt = datetime.strptime(date_start, "%Y-%m-%d")
    date_end_dt = datetime.strptime(date_end, "%Y-%m-%d")

    experience = {
        "title": title,
        "date_start": date_start_dt,
        "date_end": date_end_dt,
        "description": description,
        "company": company
    }

    experience_list.append(experience)

    return RedirectResponse("/profil", status_code=303)





