from fastapi import HTTPException, status
from src.domain.sinh_vien_repository import ISinhVienRepository
from src.schema.sinh_vien import SinhVienCreate, SinhVienUpdate, SinhVienResponse


class SinhVienService:
    def __init__(self, sinh_vien_repo: ISinhVienRepository):
        self.sinh_vien_repo = sinh_vien_repo

    def get_all(self) -> list[SinhVienResponse]:
        sinh_viens = self.sinh_vien_repo.get_all()
        return [SinhVienResponse.model_validate(sv) for sv in sinh_viens]

    def get_by_id(self, ma_sv: str) -> SinhVienResponse:
        sinh_vien = self.sinh_vien_repo.get_by_id(ma_sv)
        if not sinh_vien:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Không tìm thấy sinh viên với mã: {ma_sv}",
            )
        return SinhVienResponse.model_validate(sinh_vien)

    def create(self, data: SinhVienCreate) -> SinhVienResponse:
        existing = self.sinh_vien_repo.get_by_id(data.ma_sv)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Mã sinh viên '{data.ma_sv}' đã tồn tại",
            )
        sinh_vien = self.sinh_vien_repo.create(data)
        return SinhVienResponse.model_validate(sinh_vien)

    def update(self, ma_sv: str, data: SinhVienUpdate) -> SinhVienResponse:
        sinh_vien = self.sinh_vien_repo.get_by_id(ma_sv)
        if not sinh_vien:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Không tìm thấy sinh viên với mã: {ma_sv}",
            )
        updated = self.sinh_vien_repo.update(sinh_vien, data)
        return SinhVienResponse.model_validate(updated)

    def delete(self, ma_sv: str) -> dict:
        sinh_vien = self.sinh_vien_repo.get_by_id(ma_sv)
        if not sinh_vien:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Không tìm thấy sinh viên với mã: {ma_sv}",
            )
        self.sinh_vien_repo.delete(sinh_vien)
        return {"message": f"Đã xóa sinh viên: {ma_sv}"}
