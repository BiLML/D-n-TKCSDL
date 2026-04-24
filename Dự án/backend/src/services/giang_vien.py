from fastapi import HTTPException, status
from src.domain.giang_vien_repository import IGiangVienRepository
from src.schema.giang_vien import GiangVienCreate, GiangVienUpdate, GiangVienResponse


class GiangVienService:
    def __init__(self, giang_vien_repo: IGiangVienRepository):
        self.giang_vien_repo = giang_vien_repo

    def get_all(self) -> list[GiangVienResponse]:
        giang_viens = self.giang_vien_repo.get_all()
        return [GiangVienResponse.model_validate(gv) for gv in giang_viens]

    def get_by_id(self, ma_gv: str) -> GiangVienResponse:
        giang_vien = self.giang_vien_repo.get_by_id(ma_gv)
        if not giang_vien:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Không tìm thấy giảng viên với mã: {ma_gv}",
            )
        return GiangVienResponse.model_validate(giang_vien)

    def create(self, data: GiangVienCreate) -> GiangVienResponse:
        existing = self.giang_vien_repo.get_by_id(data.ma_gv)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Mã giảng viên '{data.ma_gv}' đã tồn tại",
            )
        giang_vien = self.giang_vien_repo.create(data)
        return GiangVienResponse.model_validate(giang_vien)

    def update(self, ma_gv: str, data: GiangVienUpdate) -> GiangVienResponse:
        giang_vien = self.giang_vien_repo.get_by_id(ma_gv)
        if not giang_vien:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Không tìm thấy giảng viên với mã: {ma_gv}",
            )
        updated = self.giang_vien_repo.update(giang_vien, data)
        return GiangVienResponse.model_validate(updated)

    def delete(self, ma_gv: str) -> dict:
        giang_vien = self.giang_vien_repo.get_by_id(ma_gv)
        if not giang_vien:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Không tìm thấy giảng viên với mã: {ma_gv}",
            )
        self.giang_vien_repo.delete(giang_vien)
        return {"message": f"Đã xóa giảng viên: {ma_gv}"}
