from typing import List, Dict, Optional
from uuid import UUID

from service.domain.quiz import Quiz
from service.domain.quiz_repository import QuizRepository


class InMemoryQuizRepository(QuizRepository):
    class __Memory:
        _instance = None
        memory: Dict = {}

    def __init__(self):
        if self.__Memory._instance is None:
            self.__Memory._instance = self.__Memory()

        self.memory: Dict = self.__Memory._instance.memory

    def flush(self) -> None:
        self.memory = {}

    def save(self, quiz: Quiz) -> None:
        self.memory[quiz.id] = quiz

    def find_all(self) -> List[Quiz]:
        all_quiz_ids = self.memory.keys()
        return [self.memory.get(quiz_id) for quiz_id in all_quiz_ids]

    def find_by_id(self, quiz_id: UUID) -> Optional[Quiz]:
        return self.memory.get(quiz_id)
