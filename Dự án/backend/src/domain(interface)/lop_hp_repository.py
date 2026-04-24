from abc import abstractmethod
from typing import Optional
from src.domain(interface).base_repository 
import IBaseRepository
from src.models.lop_hp import LopHP


class ILopHPRepository(IBaseRepository[LopHP]):
    @abstractmethod
    def get_by_id(self, ma_lop: str) -> Optional[LopHP]:
        pass
