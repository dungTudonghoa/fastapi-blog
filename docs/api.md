# HTTP API

| Method | Path | Response |
| --- | --- | --- |
| GET | `/`, `/posts` | HTML blog listing, 200 |
| GET | `/posts/{post_id}` | HTML post, 200; missing 404 |
| GET | `/api/posts` | JSON list of posts, 200 |
| GET | `/api/posts/{post_id}` | JSON post, 200; missing 404 |
| POST | `/api/posts` | JSON created post, 201; invalid payload 422 |

POST accepts `title` (string, 1–100 chars), `content` (nonempty string), `author` (string, 1–100 chars). Response includes generated integer `id` and string `date_posted`. Data is stored only in memory. OpenAPI: `/docs` and `/openapi.json`.
