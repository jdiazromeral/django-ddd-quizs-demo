import uuid
from unittest import TestCase

from service.domain.answer import Answer
from service.domain.quiz import Quiz
from service.domain.question import Question
from service.domain.skill_enum import SkillEnum


class TestQuiz(TestCase):
    def setUp(self) -> None:
        self.quiz = Quiz(
            id=uuid.uuid4(),
            title="test title",
            description="test description",
            type="test type",
            time=10,
            questions=[],
        )

        self.question_1 = Question(
            id=uuid.uuid4(),
            text="question 1 text",
            quiz_id=uuid.uuid4(),
            answers={},
            correct_anwser=[],
            skill=SkillEnum.LISTENING,
        )
        self.question_2 = Question(
            id=uuid.uuid4(),
            text="question 1 text",
            quiz_id=uuid.uuid4(),
            answers={},
            correct_anwser=[],
            skill=SkillEnum.LISTENING,
        )
        self.answer_1 = Answer(
            id=uuid.uuid4(),
            text="Answer 1 text",
            question_id=self.question_1.id,
        )
        self.answer_2 = Answer(
            id=uuid.uuid4(),
            text="Answer 1 text",
            question_id=self.question_1.id,
        )
        self.answer_3 = Answer(
            id=uuid.uuid4(),
            text="Answer 1 text",
            question_id=self.question_1.id,
        )

    def test_quiz_is_valid(self):
        self.question_1.add_answer(self.answer_1, is_valid=True)
        self.question_1.add_answer(self.answer_2)

        self.question_2.add_answer(self.answer_1, is_valid=True)

        self.quiz.add_question(self.question_1)
        self.quiz.add_question(self.question_2)

        self.assertFalse(self.quiz.is_valid())

        self.question_2.add_answer(self.answer_3)
        self.assertTrue(self.quiz.is_valid())
