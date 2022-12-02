from dataclasses import dataclass
from enum import Enum
from typing import Self


class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Result(Enum):
    LOSS = 0
    DRAW = 3
    WIN = 6


WINMAP = {
    Shape.PAPER: Shape.SCISSORS,
    Shape.SCISSORS: Shape.ROCK,
    Shape.ROCK: Shape.PAPER
}

LOSSMAP = {
    Shape.PAPER: Shape.ROCK,
    Shape.SCISSORS: Shape.PAPER,
    Shape.ROCK: Shape.SCISSORS
}

INPUTSHAPEMAP = {
    "A": Shape.ROCK,
    "B": Shape.PAPER,
    "C": Shape.SCISSORS
}

INPUTRESULTMAP = {
    "X": Result.LOSS,
    "Y": Result.DRAW,
    "Z": Result.WIN
}


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

    @staticmethod
    def shapeFromInput(input: str) -> Shape:
        return INPUTSHAPEMAP[input]

    @staticmethod
    def resultFromInput(input: str) -> Result:
        return INPUTRESULTMAP[input]

    @staticmethod
    def shapeToGetResult(opponentShape: Shape, desiredOutcome: Result) -> Shape:
        match desiredOutcome:
            case Result.DRAW:
                return opponentShape
            case Result.WIN:
                return WINMAP[opponentShape]
            case Result.LOSS:
                return LOSSMAP[opponentShape]

    @classmethod
    def fromGuide(cls, guide) -> Self:
        opponentShape = cls.shapeFromInput(guide[0])
        myShape = cls.shapeToGetResult(
            opponentShape, cls.resultFromInput(guide[2])
        )
        return cls(opponentShape=opponentShape, myShape=myShape)


with open("../input.txt", "r") as input:
    input_lines = input.readlines()

total_score = 0
for line in input_lines:
    total_score += Round.fromGuide(line).score

print(f"Total score: {total_score}")
