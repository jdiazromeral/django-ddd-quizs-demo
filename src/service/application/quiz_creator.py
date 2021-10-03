from service.domain.quiz import Quiz
from service.domain.quiz_repository import QuizRepository


class QuizCreator:
    def __init__(self, quiz_respository: QuizRepository) -> None:
        self.__quiz_respository = quiz_respository

    def create(self, quiz: Quiz) -> None:
        self.__quiz_respository.save(quiz)
