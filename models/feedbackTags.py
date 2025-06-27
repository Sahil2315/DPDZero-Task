from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

class FeedbackTags(SQLModel, table=True):
    fbtid: Optional[int] = Field(default=None, primary_key=True)
    tagid: Optional[int] = Field(default=None, foreign_key="tag.tagid") 
    fbid: Optional[int] = Field(default=None, foreign_key="feedback.fbid") 
    tag: Optional["Tag"] = Relationship(back_populates="fbtags")
    feedback: Optional["Feedback"] = Relationship(back_populates="fbtags")
    