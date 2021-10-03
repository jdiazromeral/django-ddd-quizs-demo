import uuid
from unittest import TestCase

from service.domain.answer import Answer
from service.domain.quiz import Quiz
from service.domain.question import Question
from service.domain.skill_enum import SkillEnum
from service.infrastructure.builders.answer_builder import AnswerBuilder
from service.infrastructure.builders.quiz_builder import QuizBuilder
from service.infrastructure.builders.question_builder import QuestionBuilder


class TestQuizBuilder(TestCase):
    def setUp(self) -> None:
        answer_builder = AnswerBuilder()
        question_builder = QuestionBuilder(answer_builder)
        self.quiz_builder = QuizBuilder(question_builder)

    def test_build(self):
        answer_1_id = uuid.uuid4()
        answer_2_id = uuid.uuid4()
        question_id = uuid.uuid4()
        quiz_id = uuid.uuid4()
        json = {
            "id": f"{quiz_id}",
            "title": "test title",
            "description": "test description",
            "type": "test type",
            "time": 10,
            "questions": [
                {
                    "id": f"{question_id}",
                    "text": "text question",
                    "skill": "LISTENING",
                    "answers": [
                        {
                            "id": f"{answer_1_id}",
                            "text": "answer text",
                            "question_id": f"{question_id}",
                        },
                        {
                            "id": f"{answer_2_id}",
                            "text": "answer text",
                            "question_id": f"{question_id}",
                        },
                    ],
                    "correct_answer": [f"{answer_1_id}"],
                    "quiz_id": f"{quiz_id}",
                }
            ],
        }

        expected_quiz = Quiz(
            id=quiz_id,
            title="test title",
            description="test description",
            type="test type",
            time=10,
            questions=[
                Question(
                    id=question_id,
                    text="text question",
                    skill=SkillEnum.LISTENING,
                    answers={
                        answer_1_id: Answer(answer_1_id, "answer text", question_id),
                        answer_2_id: Answer(answer_2_id, "answer text", question_id),
                    },
                    correct_anwser=[answer_1_id],
                    quiz_id=quiz_id,
                )
            ],
        )

        built_test = self.quiz_builder.build(json)
        self.assertIsInstance(built_test, Quiz)
        self.assertEqual(expected_quiz, built_test)
