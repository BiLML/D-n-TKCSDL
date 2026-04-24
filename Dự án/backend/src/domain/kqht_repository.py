from abc import ABC, abstractmethod
from typing import Optional, List, Any
from src.models.kqht import KQHT


class IKQHTRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[KQHT]:
        pass

    @abstractmethod
    def get_by_id(self, ma_sv: str, ma_lop: str) -> Optional[KQHT]:
        pass

    @abstractmethod
    def get_by_sinh_vien(self, ma_sv: str) -> List[KQHT]:
        pass

    @abstractmethod
    def get_by_lop_hp(self, ma_lop: str) -> List[KQHT]:
        pass

    @abstractmethod
    def create(self, data: Any) -> KQHT:
        pass

    @abstractmethod
    def update(self, entity: KQHT, data: Any) -> KQHT:
        pass

    @abstractmethod
    def delete(self, entity: KQHT) -> None:
        pass

    @abstractmethod
    def get_average_score(self) -> Optional[float]:
        pass
