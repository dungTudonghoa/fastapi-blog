# Use Cases — Đã triển khai

## UC-01: Kiểm tra ứng dụng phản hồi

**Actor:** HTTP client hoặc người phát triển.

**Tiền điều kiện:** server đang chạy với `main:app`.

**Luồng chính:**
1. Client gửi `GET /`.
2. FastAPI gọi handler `home()`.
3. Server trả HTTP 200 với `{"message": "Hello World"}`.

**Kết quả:** client nhận được JSON chào mừng.

**Kiểm chứng:** `tests/test_main.py`; dùng `curl http://127.0.0.1:8000/` khi server chạy.

## Chưa thuộc use case hiện hành
- Tạo, sửa, xóa hoặc liệt kê blog posts.
- Đăng nhập, phân quyền, upload file.
- Nhận hoặc phát sự kiện và gRPC.

Các trường hợp trên cần requirement và code tương ứng trước khi được mô tả là tính năng hoạt động.
