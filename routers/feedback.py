from fastapi import APIRouter, Depends
from sqlmodel import select, Session
from models.feedbackTags import FeedbackTags
from models.fbmodel import Feedback
from models.tags import Tag
from database import getSession
from collections import defaultdict
from pydantic import BaseModel
from typing import List

router = APIRouter()

@router.get("/test")
async def testerFB():
    return {"Message": "Feedback Test Message"}

@router.get("/getEmpFeedbacks/{empid}")
async def getEmpFB(empid: int, session: Session = Depends(getSession)):
    query = (
        select(Feedback, Tag)
        .join(FeedbackTags, Feedback.fbid == FeedbackTags.fbid)
        .join(Tag, Tag.tagid == FeedbackTags.tagid )
        .where(Feedback.empid == empid)
        .order_by(Feedback.fbid)

    )
    result = session.exec(query).all()
    feedback_map = defaultdict(lambda: {"tags": []})

    for fb, tag in result:
        fb_id = fb.fbid
        if "fbid" not in feedback_map[fb_id]:
            feedback_map[fb_id].update({
                "strengths": fb.strengths,
                "suggested_improvements": fb.suggestedImprovements,
                "overall": fb.overall,
                "created_at": fb.created_at.isoformat()
            })
        feedback_map[fb_id]["tags"].append(tag.tagname)

    output = list(feedback_map.values())
    return output

@router.get("/getAllTags")
async def getTags(session: Session = Depends(getSession)):
    query = (select(Tag))
    result = session.exec(query).all()
    print(result)
    output = [{"tagname": tag.tagname, "tagid": tag.tagid} for tag in result]
    return output

class feedBackInfo(BaseModel):
    empid: int
    manid: int
    overall: str
    strengths: str
    improvements: str
    tags: List[int]

@router.post("/addFeedback")
async def addFeedback(fbInfo: feedBackInfo, session: Session = Depends(getSession)):
    newFeedback = Feedback(empid=fbInfo.empid, manid = fbInfo.manid, strengths=fbInfo.strengths, suggestedImprovements=fbInfo.improvements, overall=fbInfo.overall)
    session.add(newFeedback)
    session.commit()
    session.refresh(newFeedback)
    print(newFeedback.fbid)
    for t in fbInfo.tags:
        newTag = FeedbackTags(fbid=newFeedback.fbid, tagid=t)
        session.add(newTag)
        session.commit()
    return {'success': True}