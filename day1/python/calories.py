with open("../input.txt", "r") as input:
    input_lines = input.readlines()

elves = []
elf_count = 0
for line in input_lines:
    if line.strip():
        try:
            elves[elf_count] += int(line.strip())
        except IndexError:
            elves.append(int(line.strip()))
    else:
        elf_count += 1

sorted_elves = sorted(elves, reverse=True)
# Part 1 answer
print(f"Max calories: {sorted_elves[0]}")
# Part 2 answer
print(f"Top 3 sum: {sum(sorted_elves[0:3])}")
