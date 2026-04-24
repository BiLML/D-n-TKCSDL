from typing import Generator
from fastapi import Depends
from sqlalchemy.orm import Session
from src.core.database import SessionLocal

from src.domain.mon_hoc_repository import IMonHocRepository
from src.repositories.mon_hoc import MonHocRepository
from src.services.mon_hoc import MonHocService

from src.domain.giang_vien_repository import IGiangVienRepository
from src.repositories.giang_vien import GiangVienRepository
from src.services.giang_vien import GiangVienService

from src.domain.sinh_vien_repository import ISinhVienRepository
from src.repositories.sinh_vien import SinhVienRepository
from src.services.sinh_vien import SinhVienService

from src.domain.lop_hp_repository import ILopHPRepository
from src.repositories.lop_hp import LopHPRepository
from src.services.lop_hp import LopHPService

from src.domain.kqht_repository import IKQHTRepository
from src.repositories.kqht import KQHTRepository
from src.services.kqht import KQHTService

from src.domain.giang_day_repository import IGiangDayRepository
from src.repositories.giang_day import GiangDayRepository
from src.services.giang_day import GiangDayService

from src.services.dashboard import DashboardService

# DB Dependency
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Repositories
def get_mon_hoc_repository(db: Session = Depends(get_db)) -> IMonHocRepository:
    return MonHocRepository(db)

def get_giang_vien_repository(db: Session = Depends(get_db)) -> IGiangVienRepository:
    return GiangVienRepository(db)

def get_sinh_vien_repository(db: Session = Depends(get_db)) -> ISinhVienRepository:
    return SinhVienRepository(db)

def get_lop_hp_repository(db: Session = Depends(get_db)) -> ILopHPRepository:
    return LopHPRepository(db)

def get_kqht_repository(db: Session = Depends(get_db)) -> IKQHTRepository:
    return KQHTRepository(db)

def get_giang_day_repository(db: Session = Depends(get_db)) -> IGiangDayRepository:
    return GiangDayRepository(db)


# Services
def get_mon_hoc_service(repo: IMonHocRepository = Depends(get_mon_hoc_repository)) -> MonHocService:
    return MonHocService(repo)

def get_giang_vien_service(repo: IGiangVienRepository = Depends(get_giang_vien_repository)) -> GiangVienService:
    return GiangVienService(repo)

def get_sinh_vien_service(repo: ISinhVienRepository = Depends(get_sinh_vien_repository)) -> SinhVienService:
    return SinhVienService(repo)

def get_lop_hp_service(
    lop_hp_repo: ILopHPRepository = Depends(get_lop_hp_repository),
    mon_hoc_repo: IMonHocRepository = Depends(get_mon_hoc_repository),
    giang_vien_repo: IGiangVienRepository = Depends(get_giang_vien_repository),
) -> LopHPService:
    return LopHPService(lop_hp_repo, mon_hoc_repo, giang_vien_repo)

def get_kqht_service(
    kqht_repo: IKQHTRepository = Depends(get_kqht_repository),
    sinh_vien_repo: ISinhVienRepository = Depends(get_sinh_vien_repository),
    lop_hp_repo: ILopHPRepository = Depends(get_lop_hp_repository),
) -> KQHTService:
    return KQHTService(kqht_repo, sinh_vien_repo, lop_hp_repo)

def get_giang_day_service(
    giang_day_repo: IGiangDayRepository = Depends(get_giang_day_repository),
    giang_vien_repo: IGiangVienRepository = Depends(get_giang_vien_repository),
    mon_hoc_repo: IMonHocRepository = Depends(get_mon_hoc_repository),
) -> GiangDayService:
    return GiangDayService(giang_day_repo, giang_vien_repo, mon_hoc_repo)

def get_dashboard_service(
    sinh_vien_repo: ISinhVienRepository = Depends(get_sinh_vien_repository),
    giang_vien_repo: IGiangVienRepository = Depends(get_giang_vien_repository),
    mon_hoc_repo: IMonHocRepository = Depends(get_mon_hoc_repository),
    lop_hp_repo: ILopHPRepository = Depends(get_lop_hp_repository),
    kqht_repo: IKQHTRepository = Depends(get_kqht_repository),
) -> DashboardService:
    return DashboardService(
        sinh_vien_repo, giang_vien_repo, mon_hoc_repo, lop_hp_repo, kqht_repo
    )
