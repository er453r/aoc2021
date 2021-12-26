file = open('day2.in', 'r')
commands = [dict(direction=line.split()[0], value=int(line.split()[1])) for line in file.readlines()]

forward = 0
depth = 0
aim = 0

for command in commands:
    forward += command['value'] if command['direction'] == "forward" else 0
    depth += command['value'] * aim if command['direction'] == "forward" else 0
    aim -= command['value'] if command['direction'] == "up" else 0
    aim += command['value'] if command['direction'] == "down" else 0

print(f"done - {forward * depth}")
