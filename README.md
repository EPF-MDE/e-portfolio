# Yassine Gharbi & Guillaume de Montgolfier — e-portfolio

## Overview

This project is a web application built with FastAPI to manage a personal e-portfolio.

It allows users to:
- create an account
- log in
- manage their personal profile
- add, edit, and delete professional experiences

## Tech Stack

- Language: Python
- Framework: FastAPI
- Database: SQLite (via SQLModel)
- Templating: Jinja2
- Frontend: HTML + CSS

## Features

- User authentication (login / logout)
- User creation with database persistence
- Dynamic profile page
- Full CRUD for experiences:
  - Create
  - Read
  - Update
  - Delete
- Multi-user support:
  - Each user has their own experiences
  - Data isolation between users

## Project Structure
├── core/ # Database setup
├── routers/ # Route logic (auth, user, experience)
├── schemas/ # SQLModel models
├── templates/ # HTML templates (Jinja2)
├── static/ # CSS files
├── main.py # App entry point


## Setup

### 1. Create a virtual environment

```bash
python3 -m venv env
source env/bin/activate   # Linux / Mac
env\Scripts\activate      # Windows
```
### 2.Install dependencies 

```bash
pip install -r requirements.txt
```

### 3.Run the app
```bash
fastapi dev 
```

Then open: : 
```bash
http://127.0.0.1:8000
```

## Notes
- The database is automatically created at startup
- If you modify models (e.g., add fields), delete the .db file and restart
- Passwords are currently stored in plain text (for development only)
