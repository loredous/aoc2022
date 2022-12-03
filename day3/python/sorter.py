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


with open("../input.txt", "r") as input:
    sacks = input.readlines()

sums = 0
for sack in sacks:
    rucksack = Rucksack.fromContentString(sack)
    dupes = rucksack.findDuplicates()
    for dupe in dupes:
        sums += VALUE_MAP[dupe]

print(f"Total Value: {sums}")
