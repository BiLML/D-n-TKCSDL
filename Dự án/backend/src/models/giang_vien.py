from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from src.core.database import Base


class GiangVien(Base):
    """Bảng Giảng Viên : lưu thông tin giảng viên"""

    __tablename__ = "giang_vien"

    ma_gv = Column(String(20), primary_key=True, comment="Mã giảng viên")
    ten_gv = Column(String(100), nullable=False, comment="Tên giảng viên")
    khoa = Column(String(100), nullable=True, comment="Khoa")
    email = Column(String(150), nullable=True, unique=True, comment="Email")
    sdt = Column(String(15), nullable=True, comment="Số điện thoại")

    # Relationships
    # Một giảng viên phụ trách nhiều lớp học phần
    lop_hps = relationship("LopHP", back_populates="giang_vien", lazy="selectin")

    # Quan hệ N-N với MonHoc qua bảng trung gian giang_day
    mon_hocs = relationship(
        "MonHoc",
        secondary="giang_day",
        back_populates="giang_viens",
        lazy="selectin",
    )

    def __repr__(self) -> str:
        return f"<GiangVien(ma_gv={self.ma_gv!r}, ten={self.ten_gv!r})>"
