from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from service.application.quiz_finder import QuizFinder
from service.infrastructure.repositories.in_memory_quiz_repository import InMemoryQuizRepository
from service.infrastructure.serializers.answer_serializer import AnswerSerializer
from service.infrastructure.serializers.quiz_serializer import QuizSerializer
from service.infrastructure.serializers.question_serializer import QuestionSerializer


class AllQuizFinderController(APIView):
    http_method_names = [
        "get",
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__quiz_repository = InMemoryQuizRepository()
        self.__all_quizs_finder = QuizFinder(self.__quiz_repository)
        self.__answer_serializer = AnswerSerializer()
        self.__question_serializer = QuestionSerializer(self.__answer_serializer)
        self.__quiz_serializer = QuizSerializer(self.__question_serializer)

    def get(self, request: Request, *args, **kwargs) -> Response:
        quizs = self.__all_quizs_finder.find_all()
        data = self.__quiz_serializer.serialize_all(quizs)
        return Response(status=200, data=data)
