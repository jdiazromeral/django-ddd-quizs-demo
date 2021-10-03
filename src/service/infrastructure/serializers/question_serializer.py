from typing import Dict, List
from uuid import UUID

from service.domain.question import Question
from service.domain.serializer import Serializer
from service.infrastructure.serializers.answer_serializer import AnswerSerializer


class QuestionSerializer(Serializer):
    def __init__(
        self,
        answer_serializer: AnswerSerializer,
    ) -> None:
        self.__answer_serializer = answer_serializer

    def serialize(self, item: Question) -> Dict:
        return dict(
            id=f"{item.id}",
            text=item.text,
            skill=item.skill.value,
            answers=self.__serialize_answers(item.answers),
            correct_answer=self.__serialize_correct_answer(item.correct_anwser),
            quiz_id=f"{item.quiz_id}",
        )

    def __serialize_answers(self, answers: Dict) -> Dict:
        serialized_answers = {}
        answer_keys = answers.keys()
        for answer_id in answer_keys:
            serialized_answers[f"{answer_id}"] = self.__answer_serializer.serialize(answers.get(answer_id))

        return serialized_answers

    def __serialize_correct_answer(self, answers: List[UUID]) -> List[str]:
        return [f"{answer}" for answer in answers]
