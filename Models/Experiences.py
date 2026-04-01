
from datetime import datetime
from pydantic import BaseModel

class Experience(BaseModel):
    title: str
    date_start: datetime
    date_end: datetime
    description: str
    company: str