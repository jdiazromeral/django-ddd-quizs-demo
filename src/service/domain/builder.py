from abc import ABC, abstractmethod
from typing import Any, Dict


class Builder(ABC):
    @abstractmethod
    def build(self, json: Dict) -> Any:
        pass
