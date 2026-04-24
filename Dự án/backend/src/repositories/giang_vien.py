from sqlalchemy.orm import Session
from typing import Optional, List, Any
from src.models.giang_vien import GiangVien
from src.schema.giang_vien import GiangVienCreate, GiangVienUpdate
from src.domain.giang_vien_repository import IGiangVienRepository


class GiangVienRepository(IGiangVienRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[GiangVien]:
        return self.db.query(GiangVien).all()

    def get_by_id(self, ma_gv: Any) -> Optional[GiangVien]:
        return self.db.query(GiangVien).filter(GiangVien.ma_gv == ma_gv).first()

    def create(self, data: GiangVienCreate) -> GiangVien:
        giang_vien = GiangVien(**data.model_dump())
        self.db.add(giang_vien)
        self.db.commit()
        self.db.refresh(giang_vien)
        return giang_vien

    def update(self, giang_vien: GiangVien, data: GiangVienUpdate) -> GiangVien:
        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(giang_vien, key, value)
        self.db.commit()
        self.db.refresh(giang_vien)
        return giang_vien

    def delete(self, giang_vien: GiangVien) -> None:
        self.db.delete(giang_vien)
        self.db.commit()

    def count(self) -> int:
        return self.db.query(GiangVien).count()
