from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from models.empModel import Employee
from database import getSession
from pydantic import BaseModel

router = APIRouter()

class LoginReq(BaseModel):
    username: str
    password: str

@router.get("/test")
async def testEmp():
    return {"Message": "Employee Test Message"}

@router.post("/login")
def empLogin(data: LoginReq, session: Session = Depends(getSession)):
    query = select(Employee.empid, Employee.img, Employee.name, Employee.email, Employee.phone, Employee.department, Employee.jobTitle, Employee.team, Employee.username, Employee.currentAddress, Employee.permanentAddress).where(
        Employee.username == data.username,
        Employee.password == data.password
    )
    emp = session.exec(query).first()
    if not emp:
        return {"Login": "Failed"}
    print(emp)
    return {"login": "successful", "userdata": dict(emp._mapping)}