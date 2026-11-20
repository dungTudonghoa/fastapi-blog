# fastapi-blog

FastAPI blog demo with HTML/Jinja2 pages, static assets and JSON endpoints for posts. Python >= 3.14, managed by uv. Posts are held in memory, not a database.

## Setup and run

```bash
uv sync
uv run uvicorn main:app --reload
```

Open `http://127.0.0.1:8000/` (HTML blog), `/posts`, or `/docs` (OpenAPI). Alternatively run `uv run uvicorn fastapi_blog.main:app --reload`.

## Tests

```bash
uv run python -m unittest discover -s tests -v
```

## Endpoints

| Method | Path | Function |
| --- | --- | --- |
| GET | `/`, `/posts` | Blog listing (HTML) |
| GET | `/posts/{post_id}` | Post detail (HTML) |
| GET | `/api/posts` | List posts (JSON) |
| GET | `/api/posts/{post_id}` | Get post (JSON) |
| POST | `/api/posts` | Create in-memory post (JSON) |

The implementation is `src/fastapi_blog/main.py` and `schemas.py`. `main.py` and `src/main.py` provide compatibility imports. See `AGENT.md` and `docs/` for contributor guidance. Earlier Hello World documentation was replaced when Git histories were reconciled.
