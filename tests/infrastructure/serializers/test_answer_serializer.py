import uuid
from unittest import TestCase

from service.domain.answer import Answer
from service.infrastructure.serializers.answer_serializer import AnswerSerializer


class TestAnswerSerializer(TestCase):
    def setUp(self) -> None:
        self.serializer = AnswerSerializer()

    def test_serialize(self):
        answer = Answer(id=uuid.uuid4(), text="answer text", question_id=uuid.uuid4())
        serialized_answer = self.serializer.serialize(answer)
        self.assertEqual(f"{answer.id}", serialized_answer.get("id"))
        self.assertEqual(answer.text, serialized_answer.get("text"))
        self.assertEqual(f"{answer.question_id}", serialized_answer.get("question_id"))
