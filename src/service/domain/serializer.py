from abc import ABC, abstractmethod
from typing import Any, Dict, List


class Serializer(ABC):
    @abstractmethod
    def serialize(self, item: Any) -> Dict:
        pass

    def serialize_all(self, items: List[Any]) -> List[Dict]:
        serialized_items = []
        for item in items:
            serialized_items.append(self.serialize(item))
        return serialized_items
