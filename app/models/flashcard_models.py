from dataclasses import dataclass
from enum import Enum


class DifficultyEnum(str, Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


class NonEmptyString(str):
    def __new__(cls, value: str) -> "NonEmptyString":
        if not value.strip():
            raise ValueError("String cannot be empty")
        return super().__new__(cls, value)



@dataclass(frozen=True, kw_only=True, slots=True)
class FlashCardSrc:
    difficulty_level: DifficultyEnum
    tags: list[NonEmptyString]
    front_site: NonEmptyString
    back_site: NonEmptyString
    origin: NonEmptyString

# @dataclass(frozen=True, kw_only=True, slots=True)
# class FlashCardId:
#     id: int


@dataclass(frozen=True, kw_only=True, slots=True)
class FlashCard(FlashCardSrc):
    id: int


