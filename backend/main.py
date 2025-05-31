#built-in
from contextlib import asynccontextmanager

#external
from fastapi import FastAPI
# To implement corsmiddleware.

#internal
from src.db import engine
from user.models import Base
from API.users import user_router
from API.credentials import cred_router

@asynccontextmanager
async def lifespan(_app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield
    engine.dispose()

app: FastAPI = FastAPI(lifespan = lifespan)

app.include_router(user_router)
app.include_router(cred_router)

# def want to add some unit tests at some point!

