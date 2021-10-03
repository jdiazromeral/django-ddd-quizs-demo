from typing import Dict

from service.domain.quiz import Quiz
from service.domain.serializer import Serializer
from service.infrastructure.serializers.question_serializer import QuestionSerializer


class QuizSerializer(Serializer):
    def __init__(
        self,
        question_serializer: QuestionSerializer,
    ) -> None:
        self.__question_serializer = question_serializer

    def serialize(self, item: Quiz) -> Dict:
        return dict(
            id=f"{item.id}",
            title=item.title,
            description=item.description,
            type=item.type,
            time=item.time,
            questions=self.__question_serializer.serialize_all(item.questions),
        )
