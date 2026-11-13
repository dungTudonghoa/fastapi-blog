# ADR-0001: Tách application vào src và giữ entrypoint tương thích

- **Status:** Accepted
- **Date:** 2026-11-13

## Context
Repository ban đầu chỉ có `main.py` với FastAPI `GET /`, `README.md` trống và chưa có cấu trúc tài liệu/test. Cần áp dụng quy tắc AI Agent, docs-first navigation nhưng vẫn coi code là ground truth.

## Decision
- Chuyển định nghĩa `app` và `home()` vào `src/main.py`.
- Giữ `main.py` tại root để re-export `app` và `home`.
- Bổ sung `AGENT.md`, `tests/`, `docs/` và `conversations/`.
- Chỉ document API đang hiện hữu; không triển khai API blog chưa được yêu cầu.

## Rationale (WHY)
- `src/` làm rõ vị trí code chuẩn cho AI và human.
- Adapter ở root tránh phá lệnh chạy `uvicorn main:app`.
- Test ở tầng HTTP kiểm soát regression khi thay đổi cấu trúc.
- Markdown/Mermaid dễ diff, review và đồng bộ với source.

## Consequences
- Thêm một lớp import tương thích, không đổi HTTP contract.
- Tài liệu cần cập nhật sau những thay đổi code tiếp theo.
- Giai đoạn này không mở rộng nghiệp vụ hoặc dependency.
- ADR mới cần ghi nhận những quyết định kiến trúc sau này.
