from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Tag(SQLModel, table=True):
    tagid: Optional[int] = Field(default=None, primary_key=True)
    tagname: str
    fbtags: List["FeedbackTags"] = Relationship(back_populates="tag")