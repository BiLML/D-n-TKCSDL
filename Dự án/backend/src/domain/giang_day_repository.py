from abc import ABC, abstractmethod
from typing import Optional, List, Any
from src.models.giang_day import GiangDay


class IGiangDayRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[GiangDay]:
        pass

    @abstractmethod
    def get_by_id(self, ma_gv: str, ma_mon: str) -> Optional[GiangDay]:
        pass

    @abstractmethod
    def get_by_giang_vien(self, ma_gv: str) -> List[GiangDay]:
        pass

    @abstractmethod
    def get_by_mon_hoc(self, ma_mon: str) -> List[GiangDay]:
        pass

    @abstractmethod
    def create(self, data: Any) -> GiangDay:
        pass

    @abstractmethod
    def delete(self, entity: GiangDay) -> None:
        pass
