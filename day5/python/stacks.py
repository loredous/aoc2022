
from dataclasses import dataclass, field
from typing import Self
from queue import LifoQueue


def chunk(input: str, length: int) -> list[str]:
    return [input[i:i+length] for i in range(0, len(input), length)]


@dataclass
class CargoStack(object):
    stacks: list[LifoQueue] = field(default_factory=list)

    @classmethod
    def fromDiagram(cls, diagram_lines: list[str]) -> Self:
        new = cls()
        # Get number of stacks
        indexes = diagram_lines.pop()
        size = max([
            int(stacknum) for stacknum in indexes.strip() if stacknum != " "])
        for _ in range(0, size):
            new.stacks.append(LifoQueue(maxsize=0))
        # Fill Stacks
        for line in diagram_lines[::-1]:
            boxes = chunk(line, 4)
            stackindex = 0
            for box in boxes:
                if box.startswith("["):
                    new.stacks[stackindex].put(box[1])
                stackindex += 1
        return new

    def move(self, fromindex: int, toindex: int):
        if self.stacks[fromindex].empty():
            print("wat?")
        container = self.stacks[fromindex].get()
        self.stacks[toindex].put(container)

    def execute_command(self, command: str):
        parts = command.strip().split(" ")
        count = int(parts[1])
        fromindex = int(parts[3])-1
        toindex = int(parts[5])-1
        for _ in range(count):
            self.move(fromindex, toindex)


if __name__ == "__main__":
    with open("../input.txt", "r") as infile:
        stackdata = infile.readlines()

    end_of_diagram = stackdata.index("\n")
    stack = CargoStack.fromDiagram(stackdata[0:end_of_diagram])
    instructions = stackdata[end_of_diagram+1:]
    for instruction in instructions:
        stack.execute_command(instruction)
    print("Stacking Complete!")
    final_order = ""
    for queue in stack.stacks:
        final_order += queue.get_nowait()
    print(final_order)
