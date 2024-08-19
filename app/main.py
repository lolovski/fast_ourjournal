from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.user import router as user_router
from app.api.school import router as school_router

app = FastAPI()
app.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(school_router, prefix="/school")

origins = [
    'http://localhost:5173',
    'http://127.0.0.1:5173',
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
)
