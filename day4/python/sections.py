with open("../input.txt", "r") as input:
    sections = input.readlines()

contained_count = 0
overlap_count = 0
for line in sections:
    elfa, elfb = line.strip().split(",")
    elfa_start, elfa_end = elfa.split("-")
    elfb_start, elfb_end = elfb.split("-")
    if elfa_start != elfa_end:
        elfa_set = set(range(int(elfa_start), int(elfa_end)+1))
    else:
        elfa_set = set([int(elfa_start)])
    if elfb_start != elfb_end:
        elfb_set = set(range(int(elfb_start), int(elfb_end)+1))
    else:
        elfb_set = set([int(elfb_start)])
    if elfa_set <= elfb_set or elfb_set <= elfa_set:
        contained_count += 1
    if len(elfa_set.intersection(elfb_set)) > 0:
        overlap_count += 1

print(contained_count)
print(overlap_count)
