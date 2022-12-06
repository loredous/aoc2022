def find_marker(message: str, l=4) -> int:
    window = []
    index = 0
    for chr in message:
        window.append(chr)
        index += 1
        if len(window) > l:
            window.pop(0)
        if len(set(window)) == l:
            return index


with open("../input.txt", "r") as infile:
    message = infile.read()

marker_index = find_marker(message)  # PART 1 answer
print(f"Found marker at {marker_index}")

message_index = find_marker(message, l=14)  # PART 2 answer
print(f"Found message at {message_index}")
