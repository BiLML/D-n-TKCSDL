from src.schema.mon_hoc import MonHocCreate, MonHocUpdate, MonHocResponse
from src.schema.giang_vien import GiangVienCreate, GiangVienUpdate, GiangVienResponse
from src.schema.sinh_vien import SinhVienCreate, SinhVienUpdate, SinhVienResponse
from src.schema.lop_hp import LopHPCreate, LopHPUpdate, LopHPResponse, LopHPDetailResponse
from src.schema.kqht import KQHTCreate, KQHTUpdate, KQHTResponse, KQHTDetailResponse
from src.schema.giang_day import GiangDayCreate, GiangDayResponse, GiangDayDetailResponse
from src.schema.dashboard import DashboardStats

__all__ = [
    "MonHocCreate", "MonHocUpdate", "MonHocResponse",
    "GiangVienCreate", "GiangVienUpdate", "GiangVienResponse",
    "SinhVienCreate", "SinhVienUpdate", "SinhVienResponse",
    "LopHPCreate", "LopHPUpdate", "LopHPResponse", "LopHPDetailResponse",
    "KQHTCreate", "KQHTUpdate", "KQHTResponse", "KQHTDetailResponse",
    "GiangDayCreate", "GiangDayResponse", "GiangDayDetailResponse",
    "DashboardStats",
]
