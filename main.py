from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import employee, manager, feedback
from sqlmodel import SQLModel
from database import engine
from models import empModel, mngrModel, feedbackTags, tags, fbmodel

app = FastAPI()

origins = [
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # List of allowed origins
    allow_credentials=True,  # Allow cookies and authentication headers
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

@app.on_event("startup")
def onStartup():
    SQLModel.metadata.create_all(engine)

@app.get("/")
async def apiRoot():
    return {"Message": "Test Message"}

app.include_router(employee.router, prefix = "/api/emp", tags = ["employee"])
app.include_router(manager.router, prefix = "/api/mang", tags = ["manager"])
app.include_router(feedback.router, prefix = "/api/fb", tags = ["feedback"])