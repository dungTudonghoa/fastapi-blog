# API Specification — Hiện trạng

## HTTP endpoint đang triển khai

| Method | Path | Mô tả | Status |
| --- | --- | --- | --- |
| GET | `/` | Trả về thông điệp chào mừng | 200 |

### GET /
Request: không có path parameter, query parameter hoặc request body do ứng dụng định nghĩa.

Response (200 OK, `application/json`):

```json
{
  "message": "Hello World"
}
```

Schema: object với field `message` kiểu string. Xem implementation tại `src/main.py` và test tại `tests/test_main.py`.

## API documentation tự sinh
FastAPI mặc định cung cấp `/docs` (Swagger UI), `/redoc` và `/openapi.json`. Các URL này là tài liệu framework, không phải endpoint nghiệp vụ blog.

## Các giao diện chưa có
- Chưa triển khai gRPC service.
- Chưa có protobuf file/schema.
- Chưa có HTTP endpoint cho post, author hoặc authentication.
- Không tạo contract giả định cho những giao diện chưa hiện diện.

Nếu thêm API, cần cập nhật tài liệu này từ code thực tế và ghi rõ breaking changes.
