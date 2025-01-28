from fastapi import FastAPI
from app.api.v1.endpoints import cv_parser

app = FastAPI()

app.include_router(cv_parser.router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "CV Parser API"}
