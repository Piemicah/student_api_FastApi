from fastapi import FastAPI

from data.database import Base, engine
from data.init_db import init
from endpoints import student_router

app = FastAPI()
Base.metadata.create_all(bind=engine)
init()

app.include_router(student_router.router)
