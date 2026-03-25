# Yassine Gharbi and Guillaume de Montgolfier e-portfolio 

## Outline

This project is a demonstration of web programming principles:

- language: Python
- main technology: FastAPI
- technical magic: CRUD operations in-memory and template rendering

## Subject

An e-portfolio 

## Setup

Create a virtual environmnent.

On UNIX core :

```
# Create a virtual environment
python3 -m venv env
# Activate virtual environment
source env/bin/activate
# Install dependencies
pip install -r requirements.txt
```

To run the app locally:

```
fastapi dev
```
## architecture/design
(ne pas entrer trop dans le détail)
Creer des class pour chaque "truc" (class profil(BaseModel))  -> (from pydantic import BaseModel)
form class:
class Xxx(BaseModel):
    zzz: int
    yyy: float
    uuu: bool | None = none



(majuscule pour class mais jamais pour variable)

- login  utilisateur (password secure)
- /profil  pour accéder au profil (info avec class -> id, name...)
- /profil/projet
- expérience, skill, projet
