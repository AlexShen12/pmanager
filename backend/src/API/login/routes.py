from fastapi import APIRouter, Request

from .io import LoginInfo
from src.database import Base

router: APIRouter = APIRouter()

@router.post("/signup")
def signup(inputs: LoginInfo, request: Request):
    supabase: Base = request.app.

    response = .signup(email=inputs.email, password=inputs.password)

    return response