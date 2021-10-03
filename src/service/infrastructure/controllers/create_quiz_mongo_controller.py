from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from service.application.quiz_creator import QuizCreator
from service.infrastructure.builders.answer_builder import AnswerBuilder
from service.infrastructure.builders.quiz_builder import QuizBuilder
from service.infrastructure.builders.question_builder import QuestionBuilder
from service.infrastructure.repositories.mongo_quiz_repository import MongoQuizRepository
from service.infrastructure.serializers.answer_serializer import AnswerSerializer
from service.infrastructure.serializers.quiz_serializer import QuizSerializer
from service.infrastructure.serializers.question_serializer import QuestionSerializer


class CreateQuizMongoController(APIView):
    http_method_names = [
        "post",
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__answer_serializer = AnswerSerializer()
        self.__question_serializer = QuestionSerializer(self.__answer_serializer)
        self.__quiz_serializer = QuizSerializer(self.__question_serializer)
        self.__answer_builder = AnswerBuilder()
        self.__question_builder = QuestionBuilder(self.__answer_builder)
        self.__quiz_builder = QuizBuilder(self.__question_builder)
        self.__quiz_repository = MongoQuizRepository(
            self.__quiz_serializer,
            self.__quiz_builder,
        )
        self.__quiz_creator = QuizCreator(self.__quiz_repository)

    def post(self, request: Request, *args, **kwargs) -> Response:
        json_data = request.data
        quiz = self.__quiz_builder.build(json_data)
        self.__quiz_creator.create(quiz)
        return Response(status=200)
