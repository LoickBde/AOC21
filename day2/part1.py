def read_instruction(raw_instruction):
    horizontal = 0
    depth = 0

    instruction = raw_instruction.split(" ")
    if instruction[0] == "forward":
        horizontal += int(instruction[1])
    if instruction[0] == "down":
        depth += int(instruction[1])
    if instruction[0] == "up":
        depth -= int(instruction[1])

    return horizontal, depth


horizontal = 0
depth = 0
current_h = 0
current_d = 0
with open('input/data.txt') as f:
   for line in f:
        current_h, current_d = read_instruction(line.strip())
        horizontal += current_h
        depth += current_d
        current_h = current_d = 0
        if 'str' in line:
            break

print(horizontal*depth)