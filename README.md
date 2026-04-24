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
- CRUD ops for :
  - Experiences
  - Educations
- Multi-user support:
  - Each user has their own experiences / educations 
  - Data isolation between users

## Database Design

The application uses a **relational database** with the following structure:

### User
- id (PK)
- name
- mail
- password
- etc.

### Experience
- id (PK)
- title, company, dates, etc.
- user_id (FK → User.id)

### Education
- id (PK)
- school_name, major, dates, etc.
- user_id (FK → User.id)

---

## Relationships

- **User → Experience** : 1 → N  
  → one user can have multiple experiences

- **User → Education** : 1 → N  
  → one user can have multiple education entries

👉 This means:
- each experience belongs to **one user**
- each education belongs to **one user**



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
