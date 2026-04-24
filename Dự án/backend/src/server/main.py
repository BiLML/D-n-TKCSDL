from fastapi import FastAPI
from src.middlewares.cors import setup_cors
from src.middlewares.exceptions import setup_exception_handlers
from src.controllers.mon_hoc import router as mon_hoc_router
from src.controllers.giang_vien import router as giang_vien_router
from src.controllers.sinh_vien import router as sinh_vien_router
from src.controllers.lop_hp import router as lop_hp_router
from src.controllers.kqht import router as kqht_router
from src.controllers.giang_day import router as giang_day_router
from src.controllers.dashboard import router as dashboard_router

app = FastAPI(
    title="Hệ thống Quản lý Đào tạo",
    description="API quản lý sinh viên, giảng viên, môn học, lớp học phần",
    version="1.0.0",
)

# ── Cấu hình Middlewares & Exception Handlers ───────────────
setup_cors(app)
setup_exception_handlers(app)

# ── Đăng ký các router ──────────────────────────────────────
app.include_router(mon_hoc_router)
app.include_router(giang_vien_router)
app.include_router(sinh_vien_router)
app.include_router(lop_hp_router)
app.include_router(kqht_router)
app.include_router(giang_day_router)
app.include_router(dashboard_router)


@app.get("/")
def root():
    return {"message": "Hệ thống Quản lý Đào tạo - API đang hoạt động"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
