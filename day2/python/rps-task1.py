from dataclasses import dataclass
from enum import Enum


class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Result(Enum):
    LOSS = 0
    DRAW = 3
    WIN = 6


@dataclass
class Round(object):
    opponentShape: Shape
    myShape: Shape

    @property
    def result(self) -> Result:
        if self.myShape == self.opponentShape:
            return Result.DRAW
        match self.opponentShape:
            case Shape.ROCK:
                if self.myShape == Shape.PAPER:
                    return Result.WIN
            case Shape.PAPER:
                if self.myShape == Shape.SCISSORS:
                    return Result.WIN
            case Shape.SCISSORS:
                if self.myShape == Shape.ROCK:
                    return Result.WIN
        return Result.LOSS

    @property
    def score(self) -> int:
        return self.myShape.value + self.result.value


def shapeFromInput(input: str) -> Shape:
    match input:
        case "A" | "X":
            return Shape.ROCK
        case "B" | "Y":
            return Shape.PAPER
        case "C" | "Z":
            return Shape.SCISSORS


with open("../input.txt", "r") as input:
    input_lines = input.readlines()

total_score = 0
for line in input_lines:
    total_score += Round(
        opponentShape=shapeFromInput(line[0]),
        myShape=shapeFromInput(line[2])
    ).score

print(f"Total score: {total_score}")
