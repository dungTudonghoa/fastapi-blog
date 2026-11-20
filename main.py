"""Compatibility entrypoint for `uvicorn main:app`."""
from fastapi_blog.main import app

__all__ = ["app"]
