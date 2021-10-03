from typing import Dict, List
from uuid import UUID

from service.domain.builder import Builder
from service.domain.quiz import Quiz
from service.domain.question import Question
from service.infrastructure.builders.question_builder import QuestionBuilder


class QuizBuilder(Builder):
    def __init__(
        self,
        question_builder: QuestionBuilder,
    ) -> None:
        self.__question_builder = question_builder

    def build(self, json: Dict) -> Quiz:
        return Quiz(
            id=UUID(json.get("id")),
            title=json.get("title"),
            description=json.get("description"),
            type=json.get("type"),
            time=json.get("time"),
            questions=self.__build_questions(json.get("questions")),
        )

    def __build_questions(self, questions: List[Dict]) -> List[Question]:
        built_questions = []
        for question in questions:
            built_questions.append(self.__question_builder.build(question))

        return built_questions
