from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional, List, Any

T = TypeVar('T')

class IBaseRepository(ABC, Generic[T]):
    @abstractmethod
    def get_all(self) -> List[T]:
        pass

    @abstractmethod
    def get_by_id(self, id: Any) -> Optional[T]:
        pass

    @abstractmethod
    def create(self, data: Any) -> T:
        pass

    @abstractmethod
    def update(self, entity: T, data: Any) -> T:
        pass

    @abstractmethod
    def delete(self, entity: T) -> None:
        pass

    @abstractmethod
    def count(self) -> int:
        pass
