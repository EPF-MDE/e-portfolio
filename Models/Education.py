from datetime import datetime
from pydantic import BaseModel

class Education(BaseModel):
    school_name: str
    date_start: datetime
    date_end: datetime
    description: str
    major: str