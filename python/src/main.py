from fastapi import FastAPI
from .app.interfaces.routers import user_router

app = FastAPI()

app.include_router(user_router.router)