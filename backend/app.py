
# external
from fastapi import FastAPI
from sqlalchemy import 


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

