from typing import Dict, List
from uuid import UUID

from service.domain.answer import Answer
from service.domain.builder import Builder
from service.domain.question import Question
from service.domain.skill_enum import SkillEnum
from service.infrastructure.builders.answer_builder import AnswerBuilder


class QuestionBuilder(Builder):
    def __init__(
        self,
        answer_builder: AnswerBuilder,
    ) -> None:
        self.__answer_builder = answer_builder

    def build(self, json: Dict) -> Question:
        built_question = Question(
            id=UUID(json.get("id")),
            text=json.get("text"),
            skill=SkillEnum(json.get("skill")),
            answers={},
            correct_anwser=self.__build_correct_answers(json.get("correct_answer")),
            quiz_id=UUID(json.get("quiz_id")),
        )

        answers = json.get("answers")
        if isinstance(answers, Dict):
            answers = answers.values()

        answers = self.__build_answers(answers)
        for answer in answers:
            built_question.add_answer(answer)

        return built_question

    def __build_answers(self, answers: List[Dict]) -> List[Answer]:
        built_answers = []
        for answer in answers:
            built_answers.append(self.__answer_builder.build(answer))
        return built_answers

    def __build_correct_answers(self, answer_ids: List[str]) -> List[UUID]:
        built_answer_ids = []
        for answer_id in answer_ids:
            built_answer_ids.append(UUID(answer_id))

        return built_answer_ids
