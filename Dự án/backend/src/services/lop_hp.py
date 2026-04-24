from fastapi import HTTPException, status
from src.domain.lop_hp_repository import ILopHPRepository
from src.domain.mon_hoc_repository import IMonHocRepository
from src.domain.giang_vien_repository import IGiangVienRepository
from src.schema.lop_hp import LopHPCreate, LopHPUpdate, LopHPResponse, LopHPDetailResponse


class LopHPService:
    def __init__(
        self,
        lop_hp_repo: ILopHPRepository,
        mon_hoc_repo: IMonHocRepository,
        giang_vien_repo: IGiangVienRepository,
    ):
        self.lop_hp_repo = lop_hp_repo
        self.mon_hoc_repo = mon_hoc_repo
        self.giang_vien_repo = giang_vien_repo

    def get_all(self) -> list[LopHPDetailResponse]:
        lop_hps = self.lop_hp_repo.get_all()
        results = []
        for lop in lop_hps:
            detail = LopHPDetailResponse(
                ma_lop=lop.ma_lop,
                ma_mon_hoc=lop.ma_mon_hoc,
                ma_gv=lop.ma_gv,
                thoi_gian_hoc=lop.thoi_gian_hoc,
                dia_diem_hoc=lop.dia_diem_hoc,
                ten_mon_hoc=lop.mon_hoc.ten_mon_hoc if lop.mon_hoc else None,
                ten_gv=lop.giang_vien.ten_gv if lop.giang_vien else None,
            )
            results.append(detail)
        return results

    def get_by_id(self, ma_lop: str) -> LopHPDetailResponse:
        lop = self.lop_hp_repo.get_by_id(ma_lop)
        if not lop:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Không tìm thấy lớp học phần với mã: {ma_lop}",
            )
        return LopHPDetailResponse(
            ma_lop=lop.ma_lop,
            ma_mon_hoc=lop.ma_mon_hoc,
            ma_gv=lop.ma_gv,
            thoi_gian_hoc=lop.thoi_gian_hoc,
            dia_diem_hoc=lop.dia_diem_hoc,
            ten_mon_hoc=lop.mon_hoc.ten_mon_hoc if lop.mon_hoc else None,
            ten_gv=lop.giang_vien.ten_gv if lop.giang_vien else None,
        )

    def create(self, data: LopHPCreate) -> LopHPResponse:
        # Kiểm tra lớp đã tồn tại chưa
        existing = self.lop_hp_repo.get_by_id(data.ma_lop)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Mã lớp học phần '{data.ma_lop}' đã tồn tại",
            )
        # Kiểm tra môn học tồn tại
        mon_hoc = self.mon_hoc_repo.get_by_id(data.ma_mon_hoc)
        if not mon_hoc:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Không tìm thấy môn học với mã: {data.ma_mon_hoc}",
            )
        # Kiểm tra giảng viên tồn tại (nếu có)
        if data.ma_gv:
            giang_vien = self.giang_vien_repo.get_by_id(data.ma_gv)
            if not giang_vien:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Không tìm thấy giảng viên với mã: {data.ma_gv}",
                )
        lop_hp = self.lop_hp_repo.create(data)
        return LopHPResponse.model_validate(lop_hp)

    def update(self, ma_lop: str, data: LopHPUpdate) -> LopHPResponse:
        lop_hp = self.lop_hp_repo.get_by_id(ma_lop)
        if not lop_hp:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Không tìm thấy lớp học phần với mã: {ma_lop}",
            )
        # Kiểm tra FK nếu được cập nhật
        if data.ma_mon_hoc is not None:
            mon_hoc = self.mon_hoc_repo.get_by_id(data.ma_mon_hoc)
            if not mon_hoc:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Không tìm thấy môn học với mã: {data.ma_mon_hoc}",
                )
        if data.ma_gv is not None:
            giang_vien = self.giang_vien_repo.get_by_id(data.ma_gv)
            if not giang_vien:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Không tìm thấy giảng viên với mã: {data.ma_gv}",
                )
        updated = self.lop_hp_repo.update(lop_hp, data)
        return LopHPResponse.model_validate(updated)

    def delete(self, ma_lop: str) -> dict:
        lop_hp = self.lop_hp_repo.get_by_id(ma_lop)
        if not lop_hp:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Không tìm thấy lớp học phần với mã: {ma_lop}",
            )
        self.lop_hp_repo.delete(lop_hp)
        return {"message": f"Đã xóa lớp học phần: {ma_lop}"}
