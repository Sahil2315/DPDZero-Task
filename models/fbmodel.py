from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from sqlalchemy import Column, TIMESTAMP, text
from datetime import datetime

class Feedback(SQLModel, table=True):
    fbid: Optional[int] = Field(default=None, primary_key=True)
    empid: Optional[int] = Field(default=None, foreign_key="employee.empid") 
    manid: Optional[int] = Field(default=None, foreign_key="manager.manid") 
    strengths: str
    suggestedImprovements: str
    overall: str #Positive, Negative, Neutral
    employee: Optional["Employee"] = Relationship(back_populates="feedback")
    manager: Optional["Manager"] = Relationship(back_populates="feedback")
    fbtags: List["FeedbackTags"] = Relationship(back_populates="feedback")
    created_at: datetime = Field(
        sa_column=Column(
            TIMESTAMP(timezone=True),
            nullable=False,
            server_default=text("now()")
        )
    )
