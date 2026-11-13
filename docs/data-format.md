# Data Formats — Hiện trạng

## HTTP JSON
Endpoint `GET /` phản hồi JSON object:

```json
{"message": "Hello World"}
```

| Field | Type | Ý nghĩa |
| --- | --- | --- |
| `message` | string | Thông điệp trả về từ root endpoint |

Không có request body cho `GET /`.

## Events / messages
**Chưa áp dụng:** hiện không có event producer, consumer, queue, event envelope hoặc schema serialization trong code. Không tự định nghĩa một event format khi chưa có nghiệp vụ.

## Dữ liệu tham khảo
`snippets.txt` chứa danh sách dictionary biểu diễn bài viết mẫu. File này không được runtime import, không phải storage schema và không phải API contract.

Nguồn chuẩn của payload HTTP: `src/main.py`; đối chiếu `docs/api.md`.
