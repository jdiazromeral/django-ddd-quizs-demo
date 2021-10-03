from dataclasses import dataclass
from typing import List, Dict
from uuid import UUID

from service.domain.answer import Answer
from service.domain.skill_enum import SkillEnum


@dataclass
class Question:
    id: UUID
    text: str
    skill: SkillEnum
    answers: Dict[UUID, Answer]
    correct_anwser: List[UUID]
    quiz_id: UUID

    def add_answer(
        self,
        answer: Answer,
        is_valid: bool = False,
    ) -> None:
        self.answers[answer.id] = answer
        if is_valid:
            self.correct_anwser.append(answer.id)

    def is_multiple_choice(self) -> bool:
        return len(self.answers.keys()) > 2

    def is_valid(self) -> bool:
        return all(
            [
                self.__there_are_more_questions_that_correct_answers(),
                self.__at_least_one_correct_answer(),
                self.__all_correct_answers_in_questions(),
            ]
        )

    def __there_are_more_questions_that_correct_answers(self) -> bool:
        return len(self.answers.keys()) > len(self.correct_anwser)

    def __at_least_one_correct_answer(self) -> bool:
        return len(self.correct_anwser) > 0

    def __all_correct_answers_in_questions(self) -> bool:
        return all([answer_id in self.answers.keys() for answer_id in self.correct_anwser])

    def evaluate(self, answer_ids: List[UUID]) -> bool:
        return all(
            [
                len(answer_ids) == len(self.correct_anwser),
                all([answer_id in self.correct_anwser for answer_id in answer_ids]),
            ]
        )
