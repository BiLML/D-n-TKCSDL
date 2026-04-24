from sqlalchemy.orm import Session
from typing import Optional, List, Any
from src.models.sinh_vien import SinhVien
from src.schema.sinh_vien import SinhVienCreate, SinhVienUpdate
from src.domain.sinh_vien_repository import ISinhVienRepository


class SinhVienRepository(ISinhVienRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[SinhVien]:
        return self.db.query(SinhVien).all()

    def get_by_id(self, ma_sv: Any) -> Optional[SinhVien]:
        return self.db.query(SinhVien).filter(SinhVien.ma_sv == ma_sv).first()

    def create(self, data: SinhVienCreate) -> SinhVien:
        sinh_vien = SinhVien(**data.model_dump())
        self.db.add(sinh_vien)
        self.db.commit()
        self.db.refresh(sinh_vien)
        return sinh_vien

    def update(self, sinh_vien: SinhVien, data: SinhVienUpdate) -> SinhVien:
        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(sinh_vien, key, value)
        self.db.commit()
        self.db.refresh(sinh_vien)
        return sinh_vien

    def delete(self, sinh_vien: SinhVien) -> None:
        self.db.delete(sinh_vien)
        self.db.commit()

    def count(self) -> int:
        return self.db.query(SinhVien).count()
