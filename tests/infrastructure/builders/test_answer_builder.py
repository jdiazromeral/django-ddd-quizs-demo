import uuid
from unittest import TestCase

from service.domain.answer import Answer
from service.infrastructure.builders.answer_builder import AnswerBuilder


class TestAnswerBuilder(TestCase):
    def setUp(self) -> None:
        self.builder = AnswerBuilder()

    def test_build(self):
        answer_id = uuid.uuid4()
        question_id = uuid.uuid4()
        json = {
            "id": f"{answer_id}",
            "text": "answer text",
            "question_id": f"{question_id}",
        }
        built_answer = self.builder.build(json)
        expetect_answer = Answer(
            id=answer_id,
            text="answer text",
            question_id=question_id,
        )
        self.assertIsInstance(built_answer, Answer)
        self.assertEqual(expetect_answer, built_answer)
