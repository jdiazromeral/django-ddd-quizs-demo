import uuid
from unittest import TestCase

from service.domain.answer import Answer
from service.domain.question import Question
from service.domain.skill_enum import SkillEnum


class TestQuestion(TestCase):
    def setUp(self) -> None:
        self.question_1 = Question(
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

    def test_is_multiple_choice(self):
        self.question_1.add_answer(self.answer_1)
        self.question_1.add_answer(self.answer_2)

        # question with two choices
        self.assertFalse(self.question_1.is_multiple_choice())

        # question with two or more choices
        self.question_1.add_answer(self.answer_3)
        self.assertTrue(self.question_1.is_multiple_choice())

    def test_is_valid(self):
        # no answers
        self.assertFalse(self.question_1.is_valid())

        # name of answers == name of valid answers
        self.question_1.add_answer(self.answer_1, is_valid=True)
        self.assertFalse(self.question_1.is_valid())

        # name of answers > name of valid answers
        self.question_1.add_answer(self.answer_2)
        self.assertTrue(self.question_1.is_valid())

    def test_right_answer_one_answer(self):
        self.question_1.add_answer(self.answer_1, is_valid=True)
        self.question_1.add_answer(self.answer_2)
        self.question_1.add_answer(self.answer_3)

        # invalid answer
        self.assertFalse(self.question_1.evaluate([self.answer_2.id]))

        # two answers in one answert question
        self.assertFalse(self.question_1.evaluate([self.answer_2.id, self.answer_1.id]))

        # valid answer
        self.assertTrue(self.question_1.evaluate([self.answer_1.id]))

    def test_right_answer_many_answers(self):
        self.question_1.add_answer(self.answer_1, is_valid=True)
        self.question_1.add_answer(self.answer_2, is_valid=True)
        self.question_1.add_answer(self.answer_3)

        # no answer
        self.assertFalse(self.question_1.evaluate([]))

        # only one valid answer
        self.assertFalse(self.question_1.evaluate([self.answer_2.id]))

        # one valid and one invalid
        self.assertFalse(self.question_1.evaluate([self.answer_2.id, uuid.uuid4()]))

        # two invalid answers
        self.assertFalse(self.question_1.evaluate([uuid.uuid4(), uuid.uuid4()]))

        # two valid answers
        self.assertTrue(self.question_1.evaluate([self.answer_2.id, self.answer_1.id]))
