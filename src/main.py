"""Minimal FastAPI application."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home() -> dict[str, str]:
    return {"message": "Hello World"}
