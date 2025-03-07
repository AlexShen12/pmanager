#builtin 
from contextlib import asynccontextmanager

#external 
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware


#internal
from backend.user import models
from backend.src.db import engine
from src.API.login import login_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    models.Base.metadata.create_all(bind=engine)
    yield 
    engine.dispose()

app = FastAPI(lifespan=lifespan)

origins = ["http://localhost:8080"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

app.include_router(router=login_router, prefix= "/users")

