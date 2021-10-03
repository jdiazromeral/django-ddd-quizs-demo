import uuid
from unittest import TestCase

from service.domain.answer import Answer
from service.domain.question import Question
from service.domain.skill_enum import SkillEnum
from service.infrastructure.serializers.answer_serializer import AnswerSerializer
from service.infrastructure.serializers.question_serializer import QuestionSerializer


class TestQuestionSerializer(TestCase):
    maxDiff = None

    def setUp(self) -> None:
        answer_serializer = AnswerSerializer()
        self.question_serializer = QuestionSerializer(answer_serializer)

    def test_serialize(self):
        question_1 = Question(
            id=uuid.uuid4(),
            text="text_question_1",
            skill=SkillEnum.LISTENING,
            answers={},
            correct_anwser=[],
            quiz_id=uuid.uuid4(),
        )
        answer_1 = Answer(id=uuid.uuid4(), text="text1", question_id=question_1.id)
        answer_2 = Answer(id=uuid.uuid4(), text="text2", question_id=question_1.id)
        question_1.add_answer(answer_1, is_valid=True)
        question_1.add_answer(answer_2)

        expected_serialized = {
            "id": f"{question_1.id}",
            "text": "text_question_1",
            "skill": "LISTENING",
            "answers": {
                f"{answer_1.id}": {
                    "id": f"{answer_1.id}",
                    "text": "text1",
                    "question_id": f"{question_1.id}",
                },
                f"{answer_2.id}": {
                    "id": f"{answer_2.id}",
                    "text": "text2",
                    "question_id": f"{question_1.id}",
                },
            },
            "correct_answer": [f"{answer_1.id}"],
            "quiz_id": f"{question_1.quiz_id}",
        }
        serialized = self.question_serializer.serialize(question_1)
        self.assertEqual(expected_serialized, serialized)
