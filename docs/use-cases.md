# Implemented use cases

1. Visitor opens `/` or `/posts` to browse sample posts as HTML.
2. Visitor opens `/posts/{post_id}` to view a post or receives a 404 when absent.
3. API client calls `GET /api/posts` or `GET /api/posts/{post_id}` to read JSON posts.
4. API client calls `POST /api/posts` with `author`, `title`, `content` to add a post for the life of this process.

No login or persistence use cases are implemented.
