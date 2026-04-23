from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from src.core.database import Base


class LopHP(Base):
    """Bảng Lớp Học Phần : lưu thông tin các lớp học phần"""

    __tablename__ = "lop_hp"

    ma_lop = Column(String(20), primary_key=True, comment="Mã lớp học phần")
    ma_mon_hoc = Column(
        String(20),
        ForeignKey("mon_hoc.ma_mon", ondelete="CASCADE"),
        nullable=False,
        comment="Mã môn học",
    )
    ma_gv = Column(
        String(20),
        ForeignKey("giang_vien.ma_gv", ondelete="SET NULL"),
        nullable=True,
        comment="Mã giảng viên phụ trách",
    )
    thoi_gian_hoc = Column(String(100), nullable=True, comment="Thời gian học")
    dia_diem_hoc = Column(String(200), nullable=True, comment="Địa điểm học")

    # Relationships
    mon_hoc = relationship("MonHoc", back_populates="lop_hps", lazy="selectin")
    giang_vien = relationship("GiangVien", back_populates="lop_hps", lazy="selectin")
    kqhts = relationship("KQHT", back_populates="lop_hp", lazy="selectin")

    def __repr__(self) -> str:
        return f"<LopHP(ma_lop={self.ma_lop!r})>"
