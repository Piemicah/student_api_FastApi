from fastapi import FastAPI
import uvicorn

from data.database import Base, engine
from data.init_db import init
from endpoints import auth_router, enrollment_router, payment_router, student_router, user_router

app = FastAPI()
Base.metadata.create_all(bind=engine)
init()

app.include_router(student_router.router)
app.include_router(enrollment_router.router)
app.include_router(payment_router.router)
app.include_router(auth_router.router)
app.include_router(user_router.router)

if __name__ == "__main__":

    uvicorn.run("main:app", reload=True,port=8000)
