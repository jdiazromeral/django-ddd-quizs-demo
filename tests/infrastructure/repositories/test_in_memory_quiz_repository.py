import uuid
from unittest import TestCase

from service.domain.quiz import Quiz
from service.infrastructure.repositories.in_memory_quiz_repository import InMemoryQuizRepository


class TestInMemoryQuizRepository(TestCase):
    def setUp(self) -> None:
        self.repository = InMemoryQuizRepository()
        self.repository.flush()

    def test_save(self):
        quiz_id = uuid.uuid4()
        quiz = Quiz(
            id=quiz_id,
            title="test title",
            description="test description",
            type="test type",
            time=10,
            questions=[],
        )

        self.repository.save(quiz)
        self.assertEqual(quiz, self.repository.find_by_id(quiz.id))

    def test_find_by_id(self):
        quiz_id = uuid.uuid4()
        quiz = Quiz(
            id=quiz_id,
            title="test title",
            description="test description",
            type="test type",
            time=10,
            questions=[],
        )
        self.repository.save(quiz)
        self.assertEqual(quiz, self.repository.find_by_id(quiz.id))
        self.assertIsNone(self.repository.find_by_id(uuid.uuid4()))

    def test_find_all(self):
        quiz_1 = Quiz(
            id=uuid.uuid4(),
            title="test title",
            description="test description",
            type="test type",
            time=10,
            questions=[],
        )
        quiz_2 = Quiz(
            id=uuid.uuid4(),
            title="test title",
            description="test description",
            type="test type",
            time=10,
            questions=[],
        )
        self.repository.save(quiz_1)
        self.repository.save(quiz_2)
        quizs = self.repository.find_all()
        self.assertIn(quiz_1, quizs)
        self.assertIn(quiz_2, quizs)
        self.assertEqual(2, len(quizs))
