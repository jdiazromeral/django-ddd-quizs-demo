from typing import List

from service.domain.quiz import Quiz
from service.domain.quiz_repository import QuizRepository


class QuizFinder:
    def __init__(self, quiz_respository: QuizRepository) -> None:
        self.__quiz_respository = quiz_respository

    def find_all(self) -> List[Quiz]:
        return self.__quiz_respository.find_all()
