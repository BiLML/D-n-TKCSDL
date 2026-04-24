from fastapi import HTTPException, status
from src.domain.kqht_repository import IKQHTRepository
from src.domain.sinh_vien_repository import ISinhVienRepository
from src.domain.lop_hp_repository import ILopHPRepository
from src.schema.kqht import KQHTCreate, KQHTUpdate, KQHTResponse, KQHTDetailResponse


class KQHTService:
    def __init__(
        self,
        kqht_repo: IKQHTRepository,
        sinh_vien_repo: ISinhVienRepository,
        lop_hp_repo: ILopHPRepository,
    ):
        self.kqht_repo = kqht_repo
        self.sinh_vien_repo = sinh_vien_repo
        self.lop_hp_repo = lop_hp_repo

    def get_all(self) -> list[KQHTDetailResponse]:
        kqhts = self.kqht_repo.get_all()
        results = []
        for kq in kqhts:
            detail = KQHTDetailResponse(
                ma_sv=kq.ma_sv,
                ma_lop=kq.ma_lop,
                diem_so=kq.diem_so,
                ten_sv=kq.sinh_vien.ten_sv if kq.sinh_vien else None,
                ten_mon_hoc=kq.lop_hp.mon_hoc.ten_mon_hoc if kq.lop_hp and kq.lop_hp.mon_hoc else None,
            )
            results.append(detail)
        return results

    def get_by_id(self, ma_sv: str, ma_lop: str) -> KQHTDetailResponse:
        kq = self.kqht_repo.get_by_id(ma_sv, ma_lop)
        if not kq:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Không tìm thấy kết quả học tập: SV={ma_sv}, Lớp={ma_lop}",
            )
        return KQHTDetailResponse(
            ma_sv=kq.ma_sv,
            ma_lop=kq.ma_lop,
            diem_so=kq.diem_so,
            ten_sv=kq.sinh_vien.ten_sv if kq.sinh_vien else None,
            ten_mon_hoc=kq.lop_hp.mon_hoc.ten_mon_hoc if kq.lop_hp and kq.lop_hp.mon_hoc else None,
        )

    def get_by_sinh_vien(self, ma_sv: str) -> list[KQHTDetailResponse]:
        # Kiểm tra sinh viên tồn tại
        sv = self.sinh_vien_repo.get_by_id(ma_sv)
        if not sv:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Không tìm thấy sinh viên với mã: {ma_sv}",
            )
        kqhts = self.kqht_repo.get_by_sinh_vien(ma_sv)
        results = []
        for kq in kqhts:
            detail = KQHTDetailResponse(
                ma_sv=kq.ma_sv,
                ma_lop=kq.ma_lop,
                diem_so=kq.diem_so,
                ten_sv=kq.sinh_vien.ten_sv if kq.sinh_vien else None,
                ten_mon_hoc=kq.lop_hp.mon_hoc.ten_mon_hoc if kq.lop_hp and kq.lop_hp.mon_hoc else None,
            )
            results.append(detail)
        return results

    def create(self, data: KQHTCreate) -> KQHTResponse:
        # Kiểm tra đã tồn tại
        existing = self.kqht_repo.get_by_id(data.ma_sv, data.ma_lop)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Kết quả học tập cho SV={data.ma_sv}, Lớp={data.ma_lop} đã tồn tại",
            )
        # Kiểm tra sinh viên tồn tại
        sv = self.sinh_vien_repo.get_by_id(data.ma_sv)
        if not sv:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Không tìm thấy sinh viên với mã: {data.ma_sv}",
            )
        # Kiểm tra lớp học phần tồn tại
        lop = self.lop_hp_repo.get_by_id(data.ma_lop)
        if not lop:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Không tìm thấy lớp học phần với mã: {data.ma_lop}",
            )
        kqht = self.kqht_repo.create(data)
        return KQHTResponse.model_validate(kqht)

    def update(self, ma_sv: str, ma_lop: str, data: KQHTUpdate) -> KQHTResponse:
        kqht = self.kqht_repo.get_by_id(ma_sv, ma_lop)
        if not kqht:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Không tìm thấy kết quả học tập: SV={ma_sv}, Lớp={ma_lop}",
            )
        updated = self.kqht_repo.update(kqht, data)
        return KQHTResponse.model_validate(updated)

    def delete(self, ma_sv: str, ma_lop: str) -> dict:
        kqht = self.kqht_repo.get_by_id(ma_sv, ma_lop)
        if not kqht:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Không tìm thấy kết quả học tập: SV={ma_sv}, Lớp={ma_lop}",
            )
        self.kqht_repo.delete(kqht)
        return {"message": f"Đã xóa kết quả học tập: SV={ma_sv}, Lớp={ma_lop}"}
