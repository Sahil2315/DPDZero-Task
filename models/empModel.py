from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Employee(SQLModel, table=True):
    empid: Optional[int] = Field(default=None, primary_key= True)
    name: str
    email: str
    phone: str
    department: str
    jobTitle: str
    currentAddress: str
    permanentAddress: str
    team: str
    img: str
    username: str
    password: str
    feedback: List["Feedback"] = Relationship(back_populates="employee")
