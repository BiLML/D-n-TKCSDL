from pydantic import BaseModel, ConfigDict, Field, EmailStr
from typing import Optional


class GiangVienBase(BaseModel):
    ma_gv: str = Field(..., max_length=20, description="Mã giảng viên")
    ten_gv: str = Field(..., max_length=100, description="Tên giảng viên")
    khoa: Optional[str] = Field(None, max_length=100, description="Khoa")
    email: Optional[EmailStr] = Field(None, description="Email")
    sdt: Optional[str] = Field(None, max_length=15, description="Số điện thoại")


class GiangVienCreate(GiangVienBase):
    pass


class GiangVienUpdate(BaseModel):
    ten_gv: Optional[str] = Field(None, max_length=100)
    khoa: Optional[str] = Field(None, max_length=100)
    email: Optional[EmailStr] = None
    sdt: Optional[str] = Field(None, max_length=15)


class GiangVienResponse(GiangVienBase):
    model_config = ConfigDict(from_attributes=True)
