from pydantic import BaseModel, ConfigDict, Field, EmailStr
from typing import Optional
from datetime import date


class SinhVienBase(BaseModel):
    ma_sv: str = Field(..., max_length=20, description="Mã sinh viên")
    ten_sv: str = Field(..., max_length=100, description="Tên sinh viên")
    ngay_sinh: Optional[date] = Field(None, description="Ngày sinh")
    gioi_tinh: Optional[str] = Field(None, max_length=10, description="Giới tính")
    dia_chi: Optional[str] = Field(None, max_length=255, description="Địa chỉ")
    email: Optional[EmailStr] = Field(None, description="Email")
    sdt: Optional[str] = Field(None, max_length=15, description="Số điện thoại")
    nganh_hoc: Optional[str] = Field(None, max_length=100, description="Ngành học")
    khoa: Optional[str] = Field(None, max_length=100, description="Khoa")


class SinhVienCreate(SinhVienBase):
    pass


class SinhVienUpdate(BaseModel):
    ten_sv: Optional[str] = Field(None, max_length=100)
    ngay_sinh: Optional[date] = None
    gioi_tinh: Optional[str] = Field(None, max_length=10)
    dia_chi: Optional[str] = Field(None, max_length=255)
    email: Optional[EmailStr] = None
    sdt: Optional[str] = Field(None, max_length=15)
    nganh_hoc: Optional[str] = Field(None, max_length=100)
    khoa: Optional[str] = Field(None, max_length=100)


class SinhVienResponse(SinhVienBase):
    model_config = ConfigDict(from_attributes=True)
