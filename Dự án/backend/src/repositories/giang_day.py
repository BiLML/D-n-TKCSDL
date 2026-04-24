from sqlalchemy.orm import Session
from typing import Optional, List, Any
from src.models.giang_day import GiangDay
from src.schema.giang_day import GiangDayCreate
from src.domain.giang_day_repository import IGiangDayRepository


class GiangDayRepository(IGiangDayRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[GiangDay]:
        return self.db.query(GiangDay).all()

    def get_by_id(self, ma_gv: str, ma_mon: str) -> Optional[GiangDay]:
        return self.db.query(GiangDay).filter(
            GiangDay.ma_gv == ma_gv,
            GiangDay.ma_mon == ma_mon,
        ).first()

    def get_by_giang_vien(self, ma_gv: str) -> List[GiangDay]:
        return self.db.query(GiangDay).filter(GiangDay.ma_gv == ma_gv).all()

    def get_by_mon_hoc(self, ma_mon: str) -> List[GiangDay]:
        return self.db.query(GiangDay).filter(GiangDay.ma_mon == ma_mon).all()

    def create(self, data: GiangDayCreate) -> GiangDay:
        giang_day = GiangDay(**data.model_dump())
        self.db.add(giang_day)
        self.db.commit()
        self.db.refresh(giang_day)
        return giang_day

    def delete(self, giang_day: GiangDay) -> None:
        self.db.delete(giang_day)
        self.db.commit()
