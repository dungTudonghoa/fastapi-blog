# AGENT.md — Contributor and AI agent guidance

Read in order: `AGENT.md`, `docs/architect.md`, `src/`, `tests/`, `docs/decisions/`, `docs/api.md`, `docs/data-format.md`, `docs/use-cases.md`, `docs/deployment.md`, then `conversations/` as needed.

## Principles
- Code is the source of truth; when docs differ from running code, verify code then correct docs.
- Explicit > implicit: avoid guessing scope or interfaces.
- Record WHY as well as WHAT in design decisions and ADRs.
- Prefer Markdown/Mermaid; avoid unnecessary binary artifacts.
- Do not add features outside approved scope.
- Test actual HTTP behavior, not assumptions based on repository name.

## Current application
Python >= 3.14; FastAPI/Jinja2 blog. Implementation: `src/fastapi_blog/main.py` and `src/fastapi_blog/schemas.py`; entrypoints `main.py`, `src/main.py`. HTML routes: `/`, `/posts`, `/posts/{post_id}`. JSON routes: `/api/posts`, `/api/posts/{post_id}` (GET), and `/api/posts` (POST). Static files in `static/`, templates in `templates/`. Posts are in-memory only, not durable. No authentication, database, gRPC, or event bus exists.

Run: `uv sync && uv run uvicorn main:app --reload`.
Test: `uv run python -m unittest discover -s tests -v`.
