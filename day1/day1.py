file = open('day1.in', 'r')
lines = [int(i) for i in file.readlines()]

count = 0

for n in range(1, len(lines)):
    if lines[n] - lines[n - 1] > 0:
        count += 1

print(f"done - {count}")

count = 0

for n in range(4, len(lines)):
    if lines[n] - lines[n - 3] > 0:
        count += 1

print(f"done - {count}")