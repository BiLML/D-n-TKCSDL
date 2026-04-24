from fastapi import HTTPException, status
from src.domain.giang_day_repository import IGiangDayRepository
from src.domain.giang_vien_repository import IGiangVienRepository
from src.domain.mon_hoc_repository import IMonHocRepository
from src.schema.giang_day import GiangDayCreate, GiangDayResponse, GiangDayDetailResponse


class GiangDayService:
    def __init__(
        self,
        giang_day_repo: IGiangDayRepository,
        giang_vien_repo: IGiangVienRepository,
        mon_hoc_repo: IMonHocRepository,
    ):
        self.giang_day_repo = giang_day_repo
        self.giang_vien_repo = giang_vien_repo
        self.mon_hoc_repo = mon_hoc_repo

    def get_all(self) -> list[GiangDayDetailResponse]:
        giang_days = self.giang_day_repo.get_all()
        results = []
        for gd in giang_days:
            # Lấy thông tin giảng viên và môn học
            gv = self.giang_vien_repo.get_by_id(gd.ma_gv)
            mh = self.mon_hoc_repo.get_by_id(gd.ma_mon)
            detail = GiangDayDetailResponse(
                ma_gv=gd.ma_gv,
                ma_mon=gd.ma_mon,
                ten_gv=gv.ten_gv if gv else None,
                ten_mon_hoc=mh.ten_mon_hoc if mh else None,
            )
            results.append(detail)
        return results

    def create(self, data: GiangDayCreate) -> GiangDayResponse:
        # Kiểm tra đã tồn tại
        existing = self.giang_day_repo.get_by_id(data.ma_gv, data.ma_mon)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Giảng viên {data.ma_gv} đã giảng dạy môn {data.ma_mon}",
            )
        # Kiểm tra giảng viên tồn tại
        gv = self.giang_vien_repo.get_by_id(data.ma_gv)
        if not gv:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Không tìm thấy giảng viên với mã: {data.ma_gv}",
            )
        # Kiểm tra môn học tồn tại
        mh = self.mon_hoc_repo.get_by_id(data.ma_mon)
        if not mh:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Không tìm thấy môn học với mã: {data.ma_mon}",
            )
        giang_day = self.giang_day_repo.create(data)
        return GiangDayResponse.model_validate(giang_day)

    def delete(self, ma_gv: str, ma_mon: str) -> dict:
        giang_day = self.giang_day_repo.get_by_id(ma_gv, ma_mon)
        if not giang_day:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Không tìm thấy giảng dạy: GV={ma_gv}, Môn={ma_mon}",
            )
        self.giang_day_repo.delete(giang_day)
        return {"message": f"Đã xóa giảng dạy: GV={ma_gv}, Môn={ma_mon}"}
