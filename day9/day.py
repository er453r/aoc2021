import math


def problem(input):
    file = open(input, 'r')
    readouts = [[int(i) for i in list(line.strip())] for line in file.readlines()]

    width = len(readouts[0])
    height = len(readouts)
    radius = 1

    print("width - %s" % width)
    print("height - %s" % height)

    sum = 0

    for x in range(0, width):
        for y in range(0, height):
            value = readouts[y][x]
            is_minimum = True

            # print("point - %s,%s" % (x, y))

            for nx in range(max(0, x - radius), min(width, x + radius + 1)):
                for ny in range(max(0, y - radius), min(height, y + radius + 1)):
                    if x == nx and y == ny:
                        continue

                    # print("points - %s,%s - %s,%s" % (x, y, nx, ny))

                    if readouts[ny][nx] <= value:
                        is_minimum = False
                        break

                if not is_minimum:
                    break

            if is_minimum:
                print("value - %s" % value)

                sum += 1 + value

    print("sum - %s" % sum)

    return sum


# assert (problem('day.test') == 15)
#
# print(problem('day.in'))

def basin(x, y, width, height, readouts, basin_set):
    if x < 0 or x >= width:
        return 0

    if y < 0 or y >= height:
        return 0

    value = readouts[y][x]

    if value == 9:
        return 0

    hash_ = "%s-%s" % (x, y)

    if hash_ in basin_set:
        return 0

    print("basin - (%s,%s) - %s" % (x, y, value))

    basin_set.add(hash_)

    return 1\
           + basin(x - 1, y, width, height, readouts, basin_set)\
           + basin(x + 1, y, width, height, readouts, basin_set)\
           + basin(x, y - 1, width, height, readouts, basin_set)\
           + basin(x, y + 1, width, height, readouts, basin_set)


def problem2(input):
    file = open(input, 'r')
    readouts = [[int(i) for i in list(line.strip())] for line in file.readlines()]

    width = len(readouts[0])
    height = len(readouts)
    radius = 1

    print("width - %s" % width)
    print("height - %s" % height)

    sum = 0

    basin_sizes = []

    for x in range(0, width):
        for y in range(0, height):
            value = readouts[y][x]
            is_minimum = True

            # print("point - %s,%s" % (x, y))

            for nx in range(max(0, x - radius), min(width, x + radius + 1)):
                for ny in range(max(0, y - radius), min(height, y + radius + 1)):
                    if x == nx and y == ny:
                        continue

                    # print("points - %s,%s - %s,%s" % (x, y, nx, ny))

                    if readouts[ny][nx] <= value:
                        is_minimum = False
                        break

                if not is_minimum:
                    break

            if is_minimum:
                print("minimum - %s - (%s,%s)" % (value, x, y))

                sum += 1 + value

                basin_size = basin(x, y, width, height, readouts, set())

                print("basin_size - %s" % basin_size)

                basin_sizes.append(basin_size)

    print("sum - %s" % math.prod(sorted(basin_sizes)[-3:]))

    return math.prod(sorted(basin_sizes)[-3:])


assert (problem2('day.test') == 1134)

print(problem2('day.in'))
