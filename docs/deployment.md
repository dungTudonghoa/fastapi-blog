# Deployment & Verification

## Điều kiện tiên quyết
- Python 3.12+ theo `.python-version` và `pyproject.toml`.
- `uv` đã được cài và có trên PATH.
- Đang ở thư mục gốc repository.

## Chạy local

```bash
uv sync
uv run uvicorn main:app --reload
```

Sau đó mở `http://127.0.0.1:8000/` hoặc chạy:

```bash
curl http://127.0.0.1:8000/
```

Expected: `{"message":"Hello World"}`.

## Kiểm thử

```bash
uv run python -m unittest discover -s tests -v
```

Human xác nhận output trên máy thật; không ghi “test pass” khi chưa có log thực thi.

## Chạy không có auto-reload
```bash
uv run uvicorn main:app --host 127.0.0.1 --port 8000
```

Lệnh trên chỉ là ví dụ chạy process; dự án **chưa** có Dockerfile, reverse proxy, TLS, service manager, health-check nghiệp vụ hay pipeline deployment production.

## Khi có lỗi
1. Human ghi command, môi trường Python và output gốc.
2. Human gửi stack trace/error log đã loại bỏ secrets.
3. AI phân tích code và log, đề xuất fix có WHY.
4. Human review, apply, chạy lại và gửi kết quả xác nhận.
