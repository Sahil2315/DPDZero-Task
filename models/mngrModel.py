from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Manager(SQLModel, table=True):
    manid: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    phone: str
    team: str
    img: str
    username: str
    password: str
    feedback: List["Feedback"] = Relationship(back_populates="manager")