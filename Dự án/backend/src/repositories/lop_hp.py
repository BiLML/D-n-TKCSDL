from sqlalchemy.orm import Session
from typing import Optional, List, Any
from src.models.lop_hp import LopHP
from src.schema.lop_hp import LopHPCreate, LopHPUpdate
from src.domain.lop_hp_repository import ILopHPRepository


class LopHPRepository(ILopHPRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[LopHP]:
        return self.db.query(LopHP).all()

    def get_by_id(self, ma_lop: Any) -> Optional[LopHP]:
        return self.db.query(LopHP).filter(LopHP.ma_lop == ma_lop).first()

    def create(self, data: LopHPCreate) -> LopHP:
        lop_hp = LopHP(**data.model_dump())
        self.db.add(lop_hp)
        self.db.commit()
        self.db.refresh(lop_hp)
        return lop_hp

    def update(self, lop_hp: LopHP, data: LopHPUpdate) -> LopHP:
        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(lop_hp, key, value)
        self.db.commit()
        self.db.refresh(lop_hp)
        return lop_hp

    def delete(self, lop_hp: LopHP) -> None:
        self.db.delete(lop_hp)
        self.db.commit()

    def count(self) -> int:
        return self.db.query(LopHP).count()
