from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID

from service.domain.quiz import Quiz


class QuizRepository(ABC):
    @abstractmethod
    def save(self, quiz: Quiz) -> None:
        pass

    @abstractmethod
    def find_all(self) -> List[Quiz]:
        pass

    @abstractmethod
    def find_by_id(self, quiz_id: UUID) -> Optional[Quiz]:
        pass
