from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlmodel import Session, select
from models.mngrModel import Manager
from database import getSession
from models.empModel import Employee

router = APIRouter()

class LoginReq(BaseModel):
    username: str
    password: str

@router.get("/test")
async def testMan():
    return {"Message": "Manager Test Message"}

@router.post("/login")
async def mangLogin(data: LoginReq, session: Session = Depends(getSession)):
    query = select(Manager.manid, Manager.img, Manager.name, Manager.email, Manager.phone, Manager.team, Manager.username).where(
        Manager.username == data.username,
        Manager.password == data.password
    )
    emp = session.exec(query).first()
    if not emp:
        return {"Login": "Failed"}
    print(emp)
    return {"login": "successful", "userdata": dict(emp._mapping)}

@router.get("/getTeam/{teamName}")
async def getTeam(teamName: str, session: Session = Depends(getSession)):
    query = (
        select(Employee.name, Employee.email, Employee.img, Employee.phone, Employee.jobTitle, Employee.empid)
        .where(Employee.team == teamName)
    )
    result = session.exec(query).all()
    output = [dict(row._mapping) for row in result]
    return output