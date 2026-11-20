# Data formats

Post JSON fields: `id: int`, `author: str`, `title: str`, `content: str`, `date_posted: str`. `PostCreate` requires author, title, content; `PostResponse` adds id and date_posted. Both are defined in `src/fastapi_blog/schemas.py`. GET `/api/posts` returns an array of these posts. No event schema or protobuf format is defined.
