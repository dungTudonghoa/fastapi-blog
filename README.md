# fastapi-blog

Dự án học tập FastAPI (Python >= 3.12). **Trạng thái hiện tại:** ứng dụng mới cung cấp một endpoint chào mừng, chưa có API quản lý bài viết, cơ sở dữ liệu hoặc đăng nhập.

## Yêu cầu
- Python 3.12 trở lên.
- [uv](https://docs.astral.sh/uv/) để đồng bộ môi trường theo `pyproject.toml` và `uv.lock`.

## Chạy ứng dụng

```bash
uv sync
uv run uvicorn main:app --reload
```

Mở `http://127.0.0.1:8000/` để nhận:

```json
{"message": "Hello World"}
```

FastAPI cung cấp tài liệu OpenAPI mặc định tại `/docs` và `/openapi.json`.

## Chạy kiểm thử

```bash
uv run python -m unittest discover -s tests -v
```

Các test kiểm tra HTTP response của endpoint hiện tại. Nếu chưa có `uv`, có thể cài môi trường Python tương đương theo dependency trong `pyproject.toml`.

## Cấu trúc

```text
AGENT.md                 Hướng dẫn bắt buộc cho AI Agent
main.py                  Entry point tương thích: main:app
src/main.py              FastAPI app và GET /
tests/test_main.py       Kiểm thử endpoint
docs/                    Requirements, architecture, design, API, deployment
docs/decisions/          Architecture Decision Records
conversations/           Context thảo luận (tùy chọn)
snippets.txt             Dữ liệu bài viết mẫu, chưa được dùng bởi app
```

## Tài liệu

Bắt đầu từ [AGENT.md](AGENT.md) nếu là AI Agent hoặc người đóng góp. Đọc [yêu cầu](docs/requirement.md), [kiến trúc](docs/architect.md), [thiết kế](docs/design.md), [API](docs/api.md), [data formats](docs/data-format.md), [use cases](docs/use-cases.md), [deployment](docs/deployment.md) và [ADR](docs/decisions/0001-project-structure.md) khi cần.

**Code là source of truth:** khi tài liệu xung đột với `src/`, kiểm tra hành vi ở code trước, sau đó cập nhật tài liệu. Không coi ý tưởng tương lai là feature đã triển khai.
