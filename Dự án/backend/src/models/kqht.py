from sqlalchemy import Column, String, Float, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from src.core.database import Base


class KQHT(Base):
    """Bảng Kết Quả Học Tập – lưu điểm số của sinh viên trong từng lớp học phần.

    Khóa chính tổ hợp: (ma_sv, ma_lop)
    Đây là bảng trung gian thể hiện quan hệ N-N giữa SinhVien và LopHP.
    """

    __tablename__ = "kqht"
    __table_args__ = (
        PrimaryKeyConstraint("ma_sv", "ma_lop", name="pk_kqht"),
    )

    ma_sv = Column(
        String(20),
        ForeignKey("sinh_vien.ma_sv", ondelete="CASCADE"),
        nullable=False,
        comment="Mã sinh viên",
    )
    ma_lop = Column(
        String(20),
        ForeignKey("lop_hp.ma_lop", ondelete="CASCADE"),
        nullable=False,
        comment="Mã lớp học phần",
    )
    diem_so = Column(Float, nullable=True, comment="Điểm số")

    # Relationship
    sinh_vien = relationship("SinhVien", back_populates="kqhts", lazy="selectin")
    lop_hp = relationship("LopHP", back_populates="kqhts", lazy="selectin")

    def __repr__(self) -> str:
        return f"<KQHT(ma_sv={self.ma_sv!r}, ma_lop={self.ma_lop!r}, diem={self.diem_so})>"
