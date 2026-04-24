from abc import abstractmethod
from typing import Optional
from src.domain.base_repository import IBaseRepository
from src.models.sinh_vien import SinhVien


class ISinhVienRepository(IBaseRepository[SinhVien]):
    @abstractmethod
    def get_by_id(self, ma_sv: str) -> Optional[SinhVien]:
        pass
