from sqlalchemy import Column, String, Date
from sqlalchemy.orm import relationship
from src.core.database import Base


class SinhVien(Base):
    """Bảng Sinh Viên : lưu thông tin sinh viên"""

    __tablename__ = "sinh_vien"

    ma_sv = Column(String(20), primary_key=True, comment="Mã sinh viên")
    ten_sv = Column(String(100), nullable=False, comment="Tên sinh viên")
    ngay_sinh = Column(Date, nullable=True, comment="Ngày sinh")
    gioi_tinh = Column(String(10), nullable=True, comment="Giới tính")
    dia_chi = Column(String(255), nullable=True, comment="Địa chỉ")
    email = Column(String(150), nullable=True, unique=True, comment="Email")
    sdt = Column(String(15), nullable=True, comment="Số điện thoại")
    nganh_hoc = Column(String(100), nullable=True, comment="Ngành học")
    khoa = Column(String(100), nullable=True, comment="Khoa")

    # Relationships
    # Một sinh viên có nhiều kết quả học tập
    kqhts = relationship("KQHT", back_populates="sinh_vien", lazy="selectin")

    def __repr__(self) -> str:
        return f"<SinhVien(ma_sv={self.ma_sv!r}, ten={self.ten_sv!r})>"
