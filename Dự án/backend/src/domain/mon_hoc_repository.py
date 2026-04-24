from abc import abstractmethod
from typing import Optional
from src.domain.base_repository import IBaseRepository
from src.models.mon_hoc import MonHoc


class IMonHocRepository(IBaseRepository[MonHoc]):
    @abstractmethod
    def get_by_id(self, ma_mon: str) -> Optional[MonHoc]:
        pass
