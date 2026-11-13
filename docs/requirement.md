# Requirements — Trạng thái hiện tại

## Mục tiêu đã xác minh
- RQ-01: Ứng dụng dùng Python >= 3.12 và FastAPI.
- RQ-02: HTTP GET `/` phản hồi mã 200 với JSON `{"message": "Hello World"}`.
- RQ-03: Entry point `main:app` tiếp tục hoạt động sau khi chuyển implementation vào `src/`.
- RQ-04: Cấu trúc tài liệu hỗ trợ AI đọc theo thứ tự trong `AGENT.md`.
- RQ-05: Có kiểm thử hồi quy cơ bản cho endpoint đang tồn tại.

## Ràng buộc quy trình
- Source code là ground truth nếu có xung đột với tài liệu.
- Không tự bổ sung feature ngoài yêu cầu.
- Function khoảng 50 dòng tối đa; comment nêu WHY.
- Tài liệu dùng Markdown, Mermaid, không thêm binary artifact.
- Human chạy/debug trên máy thật, AI phân tích output và đề xuất fix.

## Ngoài phạm vi hiện tại
- CRUD bài viết, authentication, database, caching và background jobs.
- gRPC, protobuf, event streaming và message queue.
- CI/CD, container deployment hay hạ tầng production.
- File `snippets.txt` chỉ là dữ liệu mẫu, không chứng minh API bài viết đã tồn tại.

## Acceptance criteria cho lần refactor này
- `GET /` giữ nguyên response và không phát sinh endpoint nghiệp vụ mới.
- Tồn tại `AGENT.md`, `README.md` và các tài liệu `docs/` yêu cầu.
- Lệnh `uvicorn main:app` không bị phá vỡ.
- Có thể chạy test bằng unittest (kết quả môi trường đích do human xác nhận).
