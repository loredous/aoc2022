import string
from typing import Self


VALUE_MAP = {string.ascii_letters[index-1]: index for index in range(1, 53)}


class Rucksack(object):
    compartments: tuple

    def __init__(self) -> None:
        self.compartments = ([], [])

    @classmethod
    def fromContentString(cls, contents: str) -> Self:
        newRucksack = cls()

        contents = contents.strip()
        half = len(contents)//2
        newRucksack.compartments[0].extend(contents[0: half])
        newRucksack.compartments[1].extend(contents[half:])
        return newRucksack

    def findDuplicates(self) -> set[str]:
        return set([item for item in self.compartments[0] if item in self.compartments[1]])

    @property
    def contents(self) -> set[str]:
        return set().union(*self.compartments)


def sack_comparator(sacks: list[Rucksack]) -> str:
    for item in sacks[0].contents:
        if item in sacks[1].contents and item in sacks[2].contents:
            return item


with open("../input.txt", "r") as input:
    sacks = input.readlines()

sums = 0
for sack in sacks:
    rucksack = Rucksack.fromContentString(sack)
    dupes = rucksack.findDuplicates()
    for dupe in dupes:
        sums += VALUE_MAP[dupe]

print(f"Total Value: {sums}")

sums = 0
while sacks:
    group = sacks[0:3]
    sack_group = []
    for sack in group:
        sacks.remove(sack)
        sack_group.append(Rucksack.fromContentString(sack))
    item = sack_comparator(sack_group)
    sums += VALUE_MAP[item]
print(f"Grouped Answer: {sums}")
