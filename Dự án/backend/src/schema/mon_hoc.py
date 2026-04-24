from pydantic import BaseModel, ConfigDict, Field
from typing import Optional


class MonHocBase(BaseModel):
    ma_mon: str = Field(..., max_length=20, description="Mã môn học")
    ten_mon_hoc: str = Field(..., max_length=100, description="Tên môn học")
    so_tin_chi: int = Field(..., gt=0, description="Số tín chỉ")


class MonHocCreate(MonHocBase):
    pass


class MonHocUpdate(BaseModel):
    ten_mon_hoc: Optional[str] = Field(None, max_length=100)
    so_tin_chi: Optional[int] = Field(None, gt=0)


class MonHocResponse(MonHocBase):
    model_config = ConfigDict(from_attributes=True)
