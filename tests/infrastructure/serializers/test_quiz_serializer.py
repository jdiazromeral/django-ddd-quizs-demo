import uuid
from unittest import TestCase

from service.domain.answer import Answer
from service.domain.quiz import Quiz
from service.domain.question import Question
from service.domain.skill_enum import SkillEnum
from service.infrastructure.serializers.answer_serializer import AnswerSerializer
from service.infrastructure.serializers.quiz_serializer import QuizSerializer
from service.infrastructure.serializers.question_serializer import QuestionSerializer


class TestQuizSerializer(TestCase):
    maxDiff = None
    def setUp(self) -> None:
        answer_serializer = AnswerSerializer()
        question_serializer = QuestionSerializer(answer_serializer)
        self.quiz_serializer = QuizSerializer(question_serializer)

    def test_serialize_no_questions(self):
        quiz = Quiz(
            id=uuid.uuid4(),
            title="quiz test title",
            description="quiz test description",
            type="test type",
            time=10,
            questions=[],
        )

        expected = {
            "id": f"{quiz.id}",
            "title": "quiz test title",
            "description": "quiz test description",
            "type": "test type",
            "time": 10,
            "questions": [],
        }
        serialized = self.quiz_serializer.serialize(quiz)
        self.assertEqual(expected, serialized)

    def test_serialize_with_questions(self):
        quiz = Quiz(
            id=uuid.uuid4(),
            title="quiz test title",
            description="quiz test description",
            type="test type",
            time=10,
            questions=[],
        )
        question_1 = Question(
            id=uuid.uuid4(),
            text="text_question_1",
            skill=SkillEnum.LISTENING,
            answers={},
            correct_anwser=[],
            quiz_id=quiz.id,
        )
        answer_1 = Answer(id=uuid.uuid4(), text="text1", question_id=question_1.id)
        answer_2 = Answer(id=uuid.uuid4(), text="text2", question_id=question_1.id)
        question_1.add_answer(answer_1, is_valid=True)
        question_1.add_answer(answer_2)

        quiz.add_question(question_1)

        expected = {
            "id": f"{quiz.id}",
            "title": "quiz test title",
            "description": "quiz test description",
            "type": "test type",
            "time": 10,
            "questions": [
                {
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
                    "quiz_id": f"{quiz.id}",
                }
            ],
        }
        serialized = self.quiz_serializer.serialize(quiz)
        self.assertEqual(expected, serialized)
