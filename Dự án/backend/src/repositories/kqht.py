from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import Optional, List, Any
from src.models.kqht import KQHT
from src.schema.kqht import KQHTCreate, KQHTUpdate
from src.domain.kqht_repository import IKQHTRepository


class KQHTRepository(IKQHTRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[KQHT]:
        return self.db.query(KQHT).all()

    def get_by_id(self, ma_sv: str, ma_lop: str) -> Optional[KQHT]:
        return self.db.query(KQHT).filter(
            KQHT.ma_sv == ma_sv,
            KQHT.ma_lop == ma_lop,
        ).first()

    def get_by_sinh_vien(self, ma_sv: str) -> List[KQHT]:
        return self.db.query(KQHT).filter(KQHT.ma_sv == ma_sv).all()

    def get_by_lop_hp(self, ma_lop: str) -> List[KQHT]:
        return self.db.query(KQHT).filter(KQHT.ma_lop == ma_lop).all()

    def create(self, data: KQHTCreate) -> KQHT:
        kqht = KQHT(**data.model_dump())
        self.db.add(kqht)
        self.db.commit()
        self.db.refresh(kqht)
        return kqht

    def update(self, kqht: KQHT, data: KQHTUpdate) -> KQHT:
        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(kqht, key, value)
        self.db.commit()
        self.db.refresh(kqht)
        return kqht

    def delete(self, kqht: KQHT) -> None:
        self.db.delete(kqht)
        self.db.commit()

    def get_average_score(self) -> Optional[float]:
        result = self.db.query(func.avg(KQHT.diem_so)).scalar()
        return round(result, 2) if result is not None else None
