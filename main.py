"""Compatibility entry point for existing `uvicorn main:app` commands."""

from src.main import app, home

__all__ = ["app", "home"]
