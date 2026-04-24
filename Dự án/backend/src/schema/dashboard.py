from pydantic import BaseModel
from typing import Optional


class DashboardStats(BaseModel):
    tong_sinh_vien: int = 0
    tong_giang_vien: int = 0
    tong_mon_hoc: int = 0
    tong_lop_hp: int = 0
    diem_trung_binh: Optional[float] = None
