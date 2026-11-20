# Implemented requirements

- Python >= 3.14 and FastAPI/Jinja2.
- Render blog listing at `/` and `/posts` and post detail at `/posts/{post_id}`.
- List, retrieve, and create posts through `/api/posts`.
- Validate post input using Pydantic; return 404 for absent posts and 422 for invalid input.
- Keep static assets under `static/` and HTML templates under `templates/`.
- No persistent database or authentication; any such functionality requires a separate scope decision.
