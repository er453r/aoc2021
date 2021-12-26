def flash(x, y, width, height, readouts, radius=1):
    if x < 0 or x >= width:
        return 0

    if y < 0 or y >= height:
        return 0

    value = readouts[y][x]

    if value <= 9:
        return 0

    sum_ = 1
    readouts[y][x] = 0

    for nx in range(max(0, x - radius), min(width, x + radius + 1)):
        for ny in range(max(0, y - radius), min(height, y + radius + 1)):
            if x == nx and y == ny:
                continue

            if readouts[ny][nx] != 0:
                readouts[ny][nx] += 1

            sum_ += flash(nx, ny, width, height, readouts)

    return sum_


def problem(input, steps):
    file = open(input, 'r')
    readouts = [[int(i) for i in list(line.strip())] for line in file.readlines()]

    width = len(readouts[0])
    height = len(readouts)
    radius = 1

    print("width - %s" % width)
    print("height - %s" % height)
    print("readouts - %s" % readouts)

    sum_ = 0

    for step in range(0, steps):
        step_flashes = 0

        for x in range(0, width):
            for y in range(0, height):
                readouts[y][x] += 1

        for x in range(0, width):
            for y in range(0, height):
                step_flashes += flash(x, y, width, height, readouts)

        if step_flashes == 100:
            print("full flash - %s" % step)

        sum_ += step_flashes

    print("sum - %s" % sum_)

    return sum_


assert (problem('day.test', 100) == 1656)

print(problem('day.in', 100))

problem('day.test', 200)
problem('day.in', 700)
