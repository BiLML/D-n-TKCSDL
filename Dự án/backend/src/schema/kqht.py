from pydantic import BaseModel, ConfigDict, Field
from typing import Optional


class KQHTBase(BaseModel):
    ma_sv: str = Field(..., max_length=20, description="Mã sinh viên")
    ma_lop: str = Field(..., max_length=20, description="Mã lớp học phần")
    diem_so: Optional[float] = Field(None, ge=0, le=10, description="Điểm số")


class KQHTCreate(KQHTBase):
    pass


class KQHTUpdate(BaseModel):
    diem_so: Optional[float] = Field(None, ge=0, le=10)


class KQHTResponse(KQHTBase):
    model_config = ConfigDict(from_attributes=True)


class KQHTDetailResponse(KQHTResponse):
    """Response kèm thông tin sinh viên và lớp học phần."""
    ten_sv: Optional[str] = None
    ten_mon_hoc: Optional[str] = None
