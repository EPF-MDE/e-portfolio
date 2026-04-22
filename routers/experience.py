from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session
from datetime import datetime

from core.database_2 import get_session
from schemas.Experiences import Experience

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/profil/experience", response_class=HTMLResponse)
def show_form(request: Request):
    return templates.TemplateResponse(request, "experience.html", {"request": request})


@router.post("/profil/experience")
def create_experience(
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

    return RedirectResponse("/profil", status_code=303)
