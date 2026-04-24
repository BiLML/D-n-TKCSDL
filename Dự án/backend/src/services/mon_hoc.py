from fastapi import HTTPException, status
from src.domain.mon_hoc_repository import IMonHocRepository
from src.schema.mon_hoc import MonHocCreate, MonHocUpdate, MonHocResponse


class MonHocService:
    def __init__(self, mon_hoc_repo: IMonHocRepository):
        self.mon_hoc_repo = mon_hoc_repo

    def get_all(self) -> list[MonHocResponse]:
        mon_hocs = self.mon_hoc_repo.get_all()
        return [MonHocResponse.model_validate(mh) for mh in mon_hocs]

    def get_by_id(self, ma_mon: str) -> MonHocResponse:
        mon_hoc = self.mon_hoc_repo.get_by_id(ma_mon)
        if not mon_hoc:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Không tìm thấy môn học với mã: {ma_mon}",
            )
        return MonHocResponse.model_validate(mon_hoc)

    def create(self, data: MonHocCreate) -> MonHocResponse:
        existing = self.mon_hoc_repo.get_by_id(data.ma_mon)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Mã môn học '{data.ma_mon}' đã tồn tại",
            )
        mon_hoc = self.mon_hoc_repo.create(data)
        return MonHocResponse.model_validate(mon_hoc)

    def update(self, ma_mon: str, data: MonHocUpdate) -> MonHocResponse:
        mon_hoc = self.mon_hoc_repo.get_by_id(ma_mon)
        if not mon_hoc:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Không tìm thấy môn học với mã: {ma_mon}",
            )
        updated = self.mon_hoc_repo.update(mon_hoc, data)
        return MonHocResponse.model_validate(updated)

    def delete(self, ma_mon: str) -> dict:
        mon_hoc = self.mon_hoc_repo.get_by_id(ma_mon)
        if not mon_hoc:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Không tìm thấy môn học với mã: {ma_mon}",
            )
        self.mon_hoc_repo.delete(mon_hoc)
        return {"message": f"Đã xóa môn học: {ma_mon}"}
