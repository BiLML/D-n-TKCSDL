from abc import abstractmethod
from typing import Optional
from src.domain.base_repository import IBaseRepository
from src.models.giang_vien import GiangVien


class IGiangVienRepository(IBaseRepository[GiangVien]):
    @abstractmethod
    def get_by_id(self, ma_gv: str) -> Optional[GiangVien]:
        pass
