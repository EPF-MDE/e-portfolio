from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session
from datetime import datetime

from core.database_2 import get_session
from schemas.Experiences import Experience

router = APIRouter()
templates = Jinja2Templates(directory="templates")


# Form CREATE
@router.get("/profil/experience", response_class=HTMLResponse)
def show_experience_form(request: Request, mail: str):
    return templates.TemplateResponse(
        request,
        "experience.html",
        {"request": request, "exp": None, "mail": mail},
    )


# CREATE
@router.post("/profil/experience")
def create_experience(
    request: Request,
    mail: str,
    title: str = Form(...),
    date_start: str = Form(...),
    date_end: str = Form(...),
    description: str = Form(...),
    company: str = Form(...),
    session: Session = Depends(get_session),
):
    experience = Experience(
        title=title,
        date_start=datetime.strptime(date_start, "%Y-%m-%d"),
        date_end=datetime.strptime(date_end, "%Y-%m-%d"),
        description=description,
        company=company,
    )

    session.add(experience)
    session.commit()

    return RedirectResponse(f"/profil?mail={mail}", status_code=303)


# DELETE
@router.post("/profil/experience/delete/{exp_id}")
def delete_experience(
    exp_id: int,
    mail: str,
    session: Session = Depends(get_session),
):
    exp = session.get(Experience, exp_id)

    if exp:
        session.delete(exp)
        session.commit()

    return RedirectResponse(f"/profil?mail={mail}", status_code=303)


# EDIT FORM
@router.get("/profil/experience/edit/{exp_id}", response_class=HTMLResponse)
def edit_experience_form(
    request: Request,
    exp_id: int,
    mail: str,
    session: Session = Depends(get_session),
):
    exp = session.get(Experience, exp_id)

    return templates.TemplateResponse(
        request,
        "experience.html",
        {"request": request, "exp": exp, "mail": mail},
    )


# UPDATE
@router.post("/profil/experience/edit/{exp_id}")
def update_experience(
    exp_id: int,
    mail: str,
    title: str = Form(...),
    date_start: str = Form(...),
    date_end: str = Form(...),
    description: str = Form(...),
    company: str = Form(...),
    session: Session = Depends(get_session),
):
    exp = session.get(Experience, exp_id)

    if exp:
        exp.title = title
        exp.date_start = datetime.strptime(date_start, "%Y-%m-%d")
        exp.date_end = datetime.strptime(date_end, "%Y-%m-%d")
        exp.description = description
        exp.company = company

        session.commit()

    return RedirectResponse(f"/profil?mail={mail}", status_code=303)
