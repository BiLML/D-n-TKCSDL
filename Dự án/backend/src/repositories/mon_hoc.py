from sqlalchemy.orm import Session
from typing import Optional, List, Any
from src.models.mon_hoc import MonHoc
from src.schema.mon_hoc import MonHocCreate, MonHocUpdate
from src.domain.mon_hoc_repository import IMonHocRepository


class MonHocRepository(IMonHocRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[MonHoc]:
        return self.db.query(MonHoc).all()

    def get_by_id(self, ma_mon: Any) -> Optional[MonHoc]:
        return self.db.query(MonHoc).filter(MonHoc.ma_mon == ma_mon).first()

    def create(self, data: MonHocCreate) -> MonHoc:
        mon_hoc = MonHoc(**data.model_dump())
        self.db.add(mon_hoc)
        self.db.commit()
        self.db.refresh(mon_hoc)
        return mon_hoc

    def update(self, mon_hoc: MonHoc, data: MonHocUpdate) -> MonHoc:
        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(mon_hoc, key, value)
        self.db.commit()
        self.db.refresh(mon_hoc)
        return mon_hoc

    def delete(self, mon_hoc: MonHoc) -> None:
        self.db.delete(mon_hoc)
        self.db.commit()

    def count(self) -> int:
        return self.db.query(MonHoc).count()
