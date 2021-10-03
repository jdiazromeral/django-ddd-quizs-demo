from dataclasses import dataclass
from typing import List
from uuid import UUID

from service.domain.question import Question


@dataclass
class Quiz:
    id: UUID
    title: str
    description: str
    type: str
    time: int
    questions: List[Question]

    def add_question(self, question: Question) -> None:
        self.questions.append(question)

    def is_valid(self) -> bool:
        return all([question.is_valid() for question in self.questions])
