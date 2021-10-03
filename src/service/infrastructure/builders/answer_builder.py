from typing import Dict
from uuid import UUID

from service.domain.answer import Answer
from service.domain.builder import Builder


class AnswerBuilder(Builder):
    def build(self, json: Dict) -> Answer:
        return Answer(
            id=UUID(json.get("id")),
            text=json.get("text"),
            question_id=UUID(json.get("question_id")),
        )
