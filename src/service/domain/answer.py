from dataclasses import dataclass
from uuid import UUID


@dataclass
class Answer:
    id: UUID
    text: str
    question_id: UUID
