# Tổng hợp Xây dựng Hệ thống Backend - Quản lý Đào tạo (QLDT)

Tài liệu này tổng hợp toàn bộ các tính năng, cấu trúc và thiết kế kiến trúc đã được triển khai cho hệ thống Backend của dự án Quản lý Đào tạo.

## 1. Công nghệ sử dụng
- **Ngôn ngữ**: Python 3.12+
- **Framework**: FastAPI (Web Framework tốc độ cao)
- **Database**: PostgreSQL
- **ORM & Database Tool**: SQLAlchemy, Alembic (quản lý Migration)
- **Data Validation**: Pydantic
- **Môi trường Deploy**: Docker & Docker Compose

## 2. Cấu trúc Cơ sở dữ liệu (Database Schema)
Hệ thống quản lý 6 thực thể (Entities) chính với các mối quan hệ chặt chẽ:
1. **Môn Học (`mon_hoc`)**: Lưu trữ thông tin môn học (Mã môn, Tên môn, Số tín chỉ).
2. **Giảng Viên (`giang_vien`)**: Lưu trữ thông tin giảng viên (Mã GV, Tên GV, Khoa/Bộ môn).
3. **Sinh Viên (`sinh_vien`)**: Lưu trữ thông tin sinh viên (Mã SV, Tên SV, Email, Ngày sinh).
4. **Lớp Học Phần (`lop_hp`)**: Liên kết Môn học và Giảng viên, chứa thông tin lớp học (Mã lớp, Thời gian, Địa điểm). 
5. **Giảng Dạy (`giang_day`)**: Quan hệ Nhiều-Nhiều giữa Giảng viên và Môn học (Giảng viên nào có thể dạy môn nào).
6. **Kết Quả Học Tập (`kqht`)**: Điểm số của Sinh viên cho từng Lớp Học Phần.

## 3. Kiến trúc Hệ thống (Clean Architecture)
Hệ thống tuân thủ nghiêm ngặt **Clean Architecture** và nguyên lý **SOLID** (đặc biệt là Dependency Inversion), chia làm các tầng riêng biệt:

- **Tầng Domain (`src/domain/`)**: 
  - Chứa các Interface/Abstract Base Class (ví dụ: `IMonHocRepository`).
  - Định nghĩa "Hợp đồng" các phương thức thao tác dữ liệu mà không quan tâm đến việc cơ sở dữ liệu thực tế là gì.
- **Tầng Repositories (`src/repositories/`)**:
  - Implement các Interface từ tầng Domain.
  - Sử dụng SQLAlchemy `Session` để thực hiện các truy vấn CRUD trực tiếp vào PostgreSQL.
- **Tầng Services (`src/services/`)**:
  - Chứa toàn bộ Business Logic (Logic nghiệp vụ).
  - Không gọi trực tiếp vào Database, mà nhận các Object Repository thông qua Dependency Injection. Xử lý các nghiệp vụ như kiểm tra trùng lặp mã, ràng buộc khóa ngoại trước khi gọi Repository để lưu.
- **Tầng Controllers (`src/controllers/`)**:
  - Chứa các FastAPI Routers (Endpoint).
  - Nhiệm vụ duy nhất là nhận HTTP Request, gọi Service tương ứng xử lý, và trả về HTTP Response.
  - Sử dụng FastAPI `Depends` để tiêm (inject) Service vào Controller.

## 4. Quản lý Dependency Injection (DI)
- Toàn bộ việc khởi tạo các kết nối Database, Repository và Service được quản lý tập trung tại `src/core/dependencies.py`.
- Tách biệt hoàn toàn việc khởi tạo Object khỏi logic sử dụng Object, giúp hệ thống dễ dàng thực hiện Unit Test (Mocking).

## 5. Middlewares & Xử lý Lỗi (Exception Handling)
- **CORS Middleware (`src/middlewares/cors.py`)**: Cấu hình bảo mật cho phép các ứng dụng Frontend (React/Vue) có thể gọi API mà không bị chặn lỗi Cross-Origin.
- **Global Exception Handler (`src/middlewares/exceptions.py`)**: Bắt toàn bộ các lỗi từ Validation (422), Logic (400, 404, 409) cho đến Lỗi Server (500) và format chúng thành một cấu trúc JSON đồng nhất chuẩn RESTful.

## 6. API Endpoints Chính
Hệ thống đã cung cấp đầy đủ các API chuẩn REST:
- **`[GET/POST/PUT/DELETE] /api/mon-hoc`**: Quản lý Môn học
- **`[GET/POST/PUT/DELETE] /api/giang-vien`**: Quản lý Giảng viên
- **`[GET/POST/PUT/DELETE] /api/sinh-vien`**: Quản lý Sinh viên
- **`[GET/POST/PUT/DELETE] /api/lop-hp`**: Quản lý Lớp học phần
- **`[GET/POST/PUT/DELETE] /api/giang-day`**: Quản lý thông tin phân công giảng dạy
- **`[GET/POST/PUT/DELETE] /api/kqht`**: Quản lý Điểm số / Kết quả học tập
- **`[GET] /api/dashboard/stats`**: Lấy số liệu thống kê tổng hợp cho trang chủ (Tổng SV, Tổng GV, Tổng Môn, Điểm trung bình...).

## 7. Môi trường & Triển khai
- Chạy hệ thống bằng 1 câu lệnh duy nhất: `docker compose up -d --build backend`.
- Hệ thống sẽ tự động build image, cấu hình container backend kết nối với container database (`qldt_db`), và mapping ra cổng `8000`.
- Tài liệu API tương tác trực quan (Swagger UI) được tự động generate tại: `http://localhost:8000/docs`.
