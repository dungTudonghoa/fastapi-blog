# Architecture

One FastAPI ASGI application in `src/fastapi_blog/main.py`. The root `main.py` and `src/main.py` expose the same app as compatibility entrypoints. `src/fastapi_blog/schemas.py` defines Pydantic post payloads. Jinja2 renders `templates/`; StaticFiles serves `static/`. `posts` is a process-local list, so restarting the server loses new posts.

```mermaid
flowchart LR
 Client[HTTP client] --> FastAPI[FastAPI app]
 FastAPI --> Web[Jinja2 templates]
 FastAPI --> API[JSON post API]
 API --> InMemory[In-memory posts]
 FastAPI --> Static[Static assets]
```

No database, authentication, gRPC, or message bus is implemented. The code is the source of truth.
