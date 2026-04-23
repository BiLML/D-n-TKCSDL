from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Hệ thống Quản lý Đào tạo",
    description="API quản lý sinh viên, giảng viên, môn học, lớp học phần",
    version="1.0.0",
)

# CORS - cho phép frontend kết nối
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Hệ thống Quản lý Đào tạo - API đang hoạt động"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
