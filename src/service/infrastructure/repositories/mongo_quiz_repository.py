from typing import Optional, List
from urllib.parse import quote_plus
from uuid import UUID

from pymongo import MongoClient

from service.domain.quiz import Quiz
from service.domain.quiz_repository import QuizRepository
from service.infrastructure.builders.quiz_builder import QuizBuilder
from service.infrastructure.serializers.quiz_serializer import QuizSerializer


class MongoQuizRepository(QuizRepository):
    def __init__(
        self,
        quiz_serializer: QuizSerializer,
        quizs_builder: QuizBuilder,
    ):
        self.__quiz_serializer = quiz_serializer
        self.__quiz_builder = quizs_builder

        self.__client = MongoClient(f"mongodb://quiz:{quote_plus('quiz-secret')}@localhost:27017/quizdb")
        self.__quizdb = self.__client.quizdb
        self.__quiz_collection = self.__quizdb.quizs

    def save(self, quiz: Quiz) -> None:
        serialized_quiz = self.__quiz_serializer.serialize(quiz)
        self.__quiz_collection.insert_one(serialized_quiz)

    def find_all(self) -> List[Quiz]:
        quizs = []
        mongo_quizs = self.__quiz_collection.find_all({})
        for quiz in mongo_quizs:
            quizs.append(self.__quiz_builder.build(quiz))

        return quizs

    def find_by_id(self, quiz_id: UUID) -> Optional[Quiz]:
        pass
