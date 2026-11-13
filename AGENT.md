# AGENT.md — Quy tắc làm việc với fastapi-blog

> Entry point dành cho AI Agent và người đóng góp.
> Phạm vi hiện tại: ứng dụng FastAPI tối giản, cung cấp GET /.
> Nguyên tắc cao nhất: code đang chạy là source of truth.

## 1. Mục đích
- Đọc file này trước khi đề xuất hoặc chỉnh sửa dự án.
- Ưu tiên tính đúng, khả năng kiểm chứng và thay đổi nhỏ.
- Không coi tên repository là bằng chứng về feature đã triển khai.
- Không suy diễn blog CRUD, database hay authentication từ tên dự án.
- Mọi thay đổi phải có lý do, phạm vi và cách kiểm chứng.
- AI hỗ trợ phân tích; con người quyết định áp dụng lên môi trường thật.

## 2. Thứ tự đọc bắt buộc
1. `AGENT.md` — rules, constraints và context.
2. `docs/architect.md` — kiến trúc tổng quan.
3. `src/` — implementation hiện hành, ground truth.
4. `tests/` — các hành vi được kiểm thử.
5. `docs/decisions/` — Architecture Decision Records (ADRs).
6. `docs/api.md` — API contract và interface đã có.
7. `docs/data-format.md` — định dạng payload và event (nếu có).
8. `docs/use-cases.md` — use cases đã được xác nhận.
9. `docs/deployment.md` — hướng dẫn chạy và triển khai.
10. `conversations/` — lịch sử thảo luận, chỉ đọc khi cần.
- Đọc thêm `docs/requirement.md` khi xác định phạm vi.
- Đọc thêm `docs/design.md` khi chuẩn bị thay đổi thiết kế.
- `README.md` là điểm khởi đầu cho người dùng, không thay thế code.

## 3. Source of truth và thứ tự ưu tiên
- Source code trong `src/` quyết định hành vi ứng dụng.
- `main.py` ở gốc chỉ giữ vai trò entrypoint tương thích.
- Test thể hiện các kỳ vọng đã kiểm chứng, không tự biến thành feature.
- Nếu documentation và code xung đột, tin code.
- Nếu tests và code xung đột, điều tra nguyên nhân trước khi sửa.
- Không sửa code chỉ để làm cho một đoạn tài liệu lỗi thời trở nên đúng.
- Cập nhật tài liệu để phản ánh hành vi thực tế sau khi kiểm chứng.
- Ghi rõ vấn đề chưa xác minh thay vì trình bày như sự thật.
- Câu trả lời của AI không có giá trị cao hơn output từ máy thật.

## 4. Quy tắc giao tiếp
- Explicit > Implicit: yêu cầu nêu rõ được ưu tiên hơn suy đoán.
- Không rõ yêu cầu hoặc có nhiều cách hiểu ảnh hưởng hành vi: hỏi lại.
- Nếu cần thực hiện ngay, chỉ chọn phương án tối thiểu, ít rủi ro.
- Trình bày giả định rõ ràng; không ngầm coi giả định là quyết định.
- Rationale matters: giải thích WHY cho mỗi quyết định kỹ thuật.
- Không chỉ mô tả WHAT hoặc liệt kê file đã sửa.
- Tách quan sát, giả thuyết, giải pháp và kết quả xác nhận.
- Không tuyên bố lỗi đã được sửa nếu chưa có bằng chứng kiểm chứng.
- Không tự ý thêm tính năng ngoài scope.
- Không thay đổi API public khi chưa có yêu cầu rõ ràng.

## 5. Bản đồ repository
- `AGENT.md`: quy tắc cho AI và contributor.
- `README.md`: giới thiệu, lệnh chạy và đường dẫn tài liệu.
- `main.py`: entrypoint tương thích `uvicorn main:app`.
- `src/main.py`: khai báo FastAPI app và route hiện có.
- `tests/`: các bài kiểm thử hành vi.
- `docs/requirement.md`: yêu cầu hiện hữu và ngoài phạm vi.
- `docs/architect.md`: các thành phần và luồng tổng quát.
- `docs/design.md`: phân rã module và quyết định thiết kế.
- `docs/decisions/`: ADR đã được ghi nhận.
- `docs/api.md`: HTTP endpoints và interfaces thực tế.
- `docs/data-format.md`: cấu trúc dữ liệu thực tế.
- `docs/use-cases.md`: kịch bản sử dụng.
- `docs/deployment.md`: setup, run, verify.
- `conversations/`: ngữ cảnh thảo luận tùy chọn.

## 6. Scope và kiến trúc hiện tại
- Runtime là Python, framework là FastAPI.
- Phiên bản Python yêu cầu: từ 3.12 trở lên.
- Dependency được xác nhận trong `pyproject.toml`.
- Ứng dụng hiện có HTTP `GET /` trả về JSON.
- Không có database hoặc persistence trong code hiện tại.
- Không có gRPC service hay protobuf schema trong code hiện tại.
- Không có event bus hoặc event schema trong code hiện tại.
- `snippets.txt` là dữ liệu tham khảo, không phải API đang chạy.
- Không tự ghép dữ liệu tham khảo vào endpoint nếu chưa được yêu cầu.
- Mọi sơ đồ kiến trúc phải phản ánh thành phần đã tồn tại.
- Phần dự kiến tương lai phải được dán nhãn “đề xuất”, không phải “đã có”.

## 7. Quy tắc viết code
- Mỗi function nên có tối đa khoảng 50 dòng.
- Khi dài hơn, tách theo trách nhiệm và ranh giới dễ kiểm thử.
- Chọn tên biến, hàm và module thể hiện rõ mục đích.
- Comment giải thích WHY; hạn chế comment kể lại WHAT.
- Không thêm abstraction chỉ vì dự đoán dự án sẽ mở rộng.
- Giữ API contract hiện tại nếu scope không yêu cầu thay đổi.
- Ưu tiên thay đổi nhỏ, dễ rollback và dễ review.
- Không sửa dependency hoặc lockfile nếu không thực sự cần.
- Không thêm thư viện chỉ để giải quyết tác vụ có thể dùng stdlib.
- Tránh side effect khi import module.
- Không hard-code credentials hoặc đường dẫn máy cá nhân.
- Giữ kiểu trả về và mã HTTP ổn định khi refactor nội bộ.

## 8. Quy tắc kiểm thử
- Đọc tests trước khi sửa logic có thể làm thay đổi hành vi.
- Thêm hoặc cập nhật test khi sửa behavior đã được yêu cầu.
- Test nên kiểm tra kết quả quan sát được, không bám implementation.
- Test chính hiện tại kiểm chứng `GET /` và JSON response.
- Chạy: `uv run python -m unittest discover -s tests -v`.
- Chạy thủ công: `uv run uvicorn main:app --reload`.
- Khi không thể chạy test, ghi rõ “chưa chạy”, không suy diễn pass.
- Không chế tạo terminal output, stack trace hoặc kết quả test.
- Phân biệt test thành công trên môi trường AI với máy thật.
- Human kiểm chứng lần cuối trên môi trường đích.
- Với regression, ghi lại input, expected và actual output.

## 9. Quy trình Human–AI khi debug
1. Human chạy hoặc debug ứng dụng trên máy thật.
2. Human cung cấp command đã chạy và môi trường liên quan.
3. Human cung cấp output gốc: error log, stack trace hoặc dmesg.
4. AI đọc log, xác định triệu chứng và mức độ chắc chắn.
5. AI liên hệ triệu chứng với đường đi thực tế trong code.
6. AI đưa ra giả thuyết nguyên nhân, nêu bằng chứng hỗ trợ.
7. AI đề xuất fix tối thiểu và giải thích WHY.
8. AI đưa ra cách kiểm tra và tiêu chí đạt.
9. Human review, quyết định apply thay đổi.
10. Human chạy lại và cung cấp output để xác nhận.
- Nếu chưa có log, chỉ đề xuất cách thu thập thông tin.
- Không mặc định AI có quyền truy cập hoặc thao tác máy thật.
- Không yêu cầu human tiết lộ token, mật khẩu, secret hoặc PII.
- Không khẳng định fix đã hoạt động khi human chưa verify.
- Với sự cố sản xuất, ưu tiên phương án có thể rollback.

## 10. Quy tắc tài liệu
- Text-first: dùng Markdown, Mermaid và code blocks.
- Không thêm ảnh nhị phân hay định dạng tài liệu binary.
- Sơ đồ Mermaid phải tương ứng với code hoặc có nhãn đề xuất.
- Tài liệu phải mô tả trạng thái hiện tại trước trạng thái mong muốn.
- Không viết “đã triển khai” cho thành phần chưa tồn tại.
- Cập nhật đường dẫn tài liệu khi di chuyển file.
- Nội dung phải đủ để người mới lần theo và tự kiểm chứng.
- Không coi lịch sử chat là nguồn tin chính khi khác với code.
- Tránh nhân đôi thông tin dễ drift; liên kết tới nguồn chính.

## 11. API và data contracts
- Kiểm tra decorator route trong `src/` trước khi sửa API docs.
- Với HTTP API, ghi method, path, status và response.
- Với gRPC hoặc protobuf, chỉ ghi specification khi có triển khai.
- Nếu chưa có gRPC, nêu rõ “chưa áp dụng”.
- Nếu chưa có event, nêu rõ “không phát sinh event”.
- Không tự định nghĩa event envelope chưa được yêu cầu.
- Mọi breaking change cần được nhận diện và chấp thuận.
- Dữ liệu thử nghiệm trong file rời không phải production schema.

## 12. Architecture Decision Records
- Lưu ADR dạng Markdown trong `docs/decisions/`.
- Đặt tên theo thứ tự tăng dần: `0001-ten-quyet-dinh.md`.
- ADR phải có Context, Decision, Rationale, Consequences.
- Ghi status như Proposed, Accepted hoặc Superseded.
- Không chỉnh sửa lại lịch sử quyết định để che thay đổi.
- Khi thay hướng, tạo ADR mới và liên kết ADR cũ.
- Chỉ tạo ADR cho quyết định kiến trúc có tác động đáng kể.
- Refactor thuần cấu trúc phải nêu tác động tương thích.

## 13. Bảo mật và thao tác an toàn
- Không commit file `.env`, token, credential hoặc private key.
- Không đưa dữ liệu nhạy cảm vào log, docs hay conversations.
- Không xóa dữ liệu hoặc thay đổi môi trường thật khi chưa duyệt.
- Đọc `.gitignore` trước khi thêm file vào Git.
- Review diff để phát hiện thay đổi ngoài phạm vi.
- Không chạy lệnh nguy hiểm chỉ dựa vào giả thuyết.
- Đề xuất lệnh rõ tác dụng, điều kiện tiên quyết và rủi ro.
- Không sửa file generated một cách tùy tiện.

## 14. Quy trình thực hiện thay đổi
1. Xác nhận mục tiêu và phạm vi người dùng yêu cầu.
2. Đọc tài liệu và code theo thứ tự tại mục 2.
3. Kiểm tra hành vi hiện tại, xác định baseline.
4. Nêu phương án tối thiểu và lý do lựa chọn.
5. Chỉ sửa những file liên quan trực tiếp.
6. Giữ nguyên khả năng tương thích nếu không có yêu cầu khác.
7. Thêm hoặc cập nhật test khi hợp lý.
8. Chạy test trong môi trường có thể truy cập.
9. Soát lại public API, cấu hình và dependency.
10. Đồng bộ tài liệu với implementation.
11. Ghi ADR nếu phát sinh quyết định kiến trúc.
12. Báo cáo file thay đổi, rủi ro và cách verify.
13. Để human review và apply lên môi trường đích.

## 15. Definition of done
- Yêu cầu được thực hiện đúng phạm vi.
- Code thực tế khớp API và use case đã xác nhận.
- Không tồn tại feature mới ngoài yêu cầu.
- Test được chạy hoặc trạng thái chưa chạy được công khai.
- Tài liệu và code không mâu thuẫn về hành vi hiện tại.
- Mọi quyết định quan trọng đều có WHY.
- Không chứa bí mật hoặc artifact nhị phân ngoài ý muốn.
- Có hướng dẫn verify và rollback khi cần.
- Human xác nhận hoàn tất trên máy hoặc môi trường đích.
