def read_instruction(raw_instruction, horizontal, depth, aim):
    instruction = raw_instruction.split(" ")
    command = instruction[0]
    value = int(instruction[1])

    if command == "forward":
        horizontal += value
        depth += aim*value
    if command == "down":
        aim += value
    if command == "up":
        aim -= value

    return horizontal, depth, aim


horizontal = 0
depth = 0
aim = 0
with open('input/data.txt') as f:
   for line in f:
        horizontal, depth, aim = read_instruction(line.strip(), horizontal, depth, aim)
        if 'str' in line:
            break

print(horizontal*depth)