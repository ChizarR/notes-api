from typing import Dict

from pydantic import BaseModel

from datetime import datetime


class NoteView(BaseModel):
    user_id: int
    date: datetime
    answers: Dict
