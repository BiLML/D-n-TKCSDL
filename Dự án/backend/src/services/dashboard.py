from src.domain.sinh_vien_repository import ISinhVienRepository
from src.domain.giang_vien_repository import IGiangVienRepository
from src.domain.mon_hoc_repository import IMonHocRepository
from src.domain.lop_hp_repository import ILopHPRepository
from src.domain.kqht_repository import IKQHTRepository
from src.schema.dashboard import DashboardStats


class DashboardService:
    def __init__(
        self,
        sinh_vien_repo: ISinhVienRepository,
        giang_vien_repo: IGiangVienRepository,
        mon_hoc_repo: IMonHocRepository,
        lop_hp_repo: ILopHPRepository,
        kqht_repo: IKQHTRepository,
    ):
        self.sinh_vien_repo = sinh_vien_repo
        self.giang_vien_repo = giang_vien_repo
        self.mon_hoc_repo = mon_hoc_repo
        self.lop_hp_repo = lop_hp_repo
        self.kqht_repo = kqht_repo

    def get_stats(self) -> DashboardStats:
        return DashboardStats(
            tong_sinh_vien=self.sinh_vien_repo.count(),
            tong_giang_vien=self.giang_vien_repo.count(),
            tong_mon_hoc=self.mon_hoc_repo.count(),
            tong_lop_hp=self.lop_hp_repo.count(),
            diem_trung_binh=self.kqht_repo.get_average_score(),
        )
