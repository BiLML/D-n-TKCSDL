from pydantic import BaseModel, ConfigDict, Field
from typing import Optional


class LopHPBase(BaseModel):
    ma_lop: str = Field(..., max_length=20, description="Mã lớp học phần")
    ma_mon_hoc: str = Field(..., max_length=20, description="Mã môn học")
    ma_gv: Optional[str] = Field(None, max_length=20, description="Mã giảng viên")
    thoi_gian_hoc: Optional[str] = Field(None, max_length=100, description="Thời gian học")
    dia_diem_hoc: Optional[str] = Field(None, max_length=200, description="Địa điểm học")


class LopHPCreate(LopHPBase):
    pass


class LopHPUpdate(BaseModel):
    ma_mon_hoc: Optional[str] = Field(None, max_length=20)
    ma_gv: Optional[str] = Field(None, max_length=20)
    thoi_gian_hoc: Optional[str] = Field(None, max_length=100)
    dia_diem_hoc: Optional[str] = Field(None, max_length=200)


class LopHPResponse(LopHPBase):
    model_config = ConfigDict(from_attributes=True)


class LopHPDetailResponse(LopHPResponse):
    """Response kèm thông tin môn học và giảng viên."""
    ten_mon_hoc: Optional[str] = None
    ten_gv: Optional[str] = None
