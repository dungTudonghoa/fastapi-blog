## Tôi muốn xây dựng một Web API bằng Python sử dụng framework FastAPI. Làm thế nào để đưa thư viện FastAPI vào chương trình Python để sử dụng?
from fastapi import FastAPI

## Tôi tạo một ứng dụng FastAPI để quản lý các API endpoint như thế nào?
app = FastAPI() # Có thể sử dụng APIRouter() sau khi mở rộng. 

## Khi client gửi HTTP GET request tới URL nào thì gọi hàm xử lý nào?"
@app.get("/")

## Khi API này được gọi thì server phải xử lý logic gì?
def home():
    return {"message": "Hello World"}

# async def home(): 
# uv = uvicorn là môi trường ảo để chạy ứng dụng FastAPI.
# Mỗi khi sửa lệnh -> chạy lại từ đầu uv 