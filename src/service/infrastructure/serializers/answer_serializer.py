from typing import Dict

from service.domain.answer import Answer
from service.domain.serializer import Serializer


class AnswerSerializer(Serializer):
    def serialize(self, item: Answer) -> Dict:
        return dict(
            id=f"{item.id}",
            text=item.text,
            question_id=f"{item.question_id}",
        )
