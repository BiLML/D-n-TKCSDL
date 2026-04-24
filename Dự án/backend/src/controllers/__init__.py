from src.controllers.mon_hoc import router as mon_hoc_router
from src.controllers.giang_vien import router as giang_vien_router
from src.controllers.sinh_vien import router as sinh_vien_router
from src.controllers.lop_hp import router as lop_hp_router
from src.controllers.kqht import router as kqht_router
from src.controllers.giang_day import router as giang_day_router
from src.controllers.dashboard import router as dashboard_router

__all__ = [
    "mon_hoc_router",
    "giang_vien_router",
    "sinh_vien_router",
    "lop_hp_router",
    "kqht_router",
    "giang_day_router",
    "dashboard_router",
]
