# Design

Implementation resides in `src/fastapi_blog/main.py` with Pydantic models in `src/fastapi_blog/schemas.py`. Compatibility ASGI imports live in root `main.py` and `src/main.py`. HTML pages use Jinja2 (`templates/`), while `/api/posts` serves JSON. Static content is mounted at `/static`. The mutable list of sample posts is deliberately in-memory for this learning/demo project. The current route handlers are not split into service/repository layers.
