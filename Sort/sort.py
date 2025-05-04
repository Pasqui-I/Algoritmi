from abc import ABC, abstractmethod
from typing import Any

class Sort(ABC):
    @abstractmethod
    def sort(self, array: list[Any]) -> list[Any] | None:
        pass