from sqlalchemy import Column, String, ForeignKey, Table, PrimaryKeyConstraint
from src.core.database import Base


class GiangDay(Base):
    """Bảng trung gian Giảng Dạy: thể hiện quan hệ N-N giữa GiangVien và MonHoc.

    Khóa chính tổ hợp: (ma_gv, ma_mon)
    """

    __tablename__ = "giang_day"
    __table_args__ = (
        PrimaryKeyConstraint("ma_gv", "ma_mon", name="pk_giang_day"),
    )

    ma_gv = Column(
        String(20),
        ForeignKey("giang_vien.ma_gv", ondelete="CASCADE"),
        nullable=False,
        comment="Mã giảng viên",
    )
    ma_mon = Column(
        String(20),
        ForeignKey("mon_hoc.ma_mon", ondelete="CASCADE"),
        nullable=False,
        comment="Mã môn học",
    )

    def __repr__(self) -> str:
        return f"<GiangDay(ma_gv={self.ma_gv!r}, ma_mon={self.ma_mon!r})>"
