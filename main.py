from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from data.database import Base, engine
from data.init_db import init
from endpoints import auth_router, enrollment_router, payment_router, student_router, user_router

app = FastAPI()
Base.metadata.create_all(bind=engine)
init()
# CORS
origins = [
    "http://localhost:5173",   # React (Vite)
    "http://localhost:3000",   # React (CRA)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,   # 🔥 REQUIRED for cookies
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(student_router.router)
app.include_router(enrollment_router.router)
app.include_router(payment_router.router)
app.include_router(auth_router.router)
app.include_router(user_router.router)

if __name__ == "__main__":

    uvicorn.run("main:app", reload=True,port=8000)
