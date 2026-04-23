from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from src.core.database import Base


class MonHoc(Base):
    """Bảng Môn Học: lưu thông tin các môn học trong hệ thống."""

    __tablename__ = "mon_hoc"

    ma_mon = Column(String(20), primary_key=True, comment="Mã môn học")
    ten_mon_hoc = Column(String(100), nullable=False, comment="Tên môn học")
    so_tin_chi = Column(Integer, nullable=False, comment="Số tín chỉ")

    # ── Relationships ──────────────────────────────────────────────
    # Một môn học có nhiều lớp học phần
    lop_hps = relationship("LopHP", back_populates="mon_hoc", lazy="selectin")

    # Quan hệ N-N với GiangVien qua bảng trung gian giang_day
    giang_viens = relationship(
        "GiangVien",
        secondary="giang_day",
        back_populates="mon_hocs",
        lazy="selectin",
    )

    def __repr__(self) -> str:
        return f"<MonHoc(ma_mon={self.ma_mon!r}, ten={self.ten_mon_hoc!r})>"
