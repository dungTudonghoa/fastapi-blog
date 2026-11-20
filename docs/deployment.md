# Local deployment and verification

Requirements: Python >= 3.14, uv. At repository root:

```bash
uv sync
uv run uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000/` for HTML or `http://127.0.0.1:8000/docs` for OpenAPI.

```bash
uv run python -m unittest discover -s tests -v
```

Caution: posts persist only in process memory; no production database, authentication or deployment pipeline is configured.
