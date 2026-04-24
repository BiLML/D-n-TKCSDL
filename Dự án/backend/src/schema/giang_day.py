from pydantic import BaseModel, ConfigDict, Field
from typing import Optional


class GiangDayBase(BaseModel):
    ma_gv: str = Field(..., max_length=20, description="Mã giảng viên")
    ma_mon: str = Field(..., max_length=20, description="Mã môn học")


class GiangDayCreate(GiangDayBase):
    pass


class GiangDayResponse(GiangDayBase):
    model_config = ConfigDict(from_attributes=True)


class GiangDayDetailResponse(GiangDayResponse):
    """Response kèm thông tin giảng viên và môn học."""
    ten_gv: Optional[str] = None
    ten_mon_hoc: Optional[str] = None
