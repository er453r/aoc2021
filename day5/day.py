def problem(input):
    file = open(input, 'r')
    lines = [line.strip().split(" -> ") for line in file.readlines()]

    print("lines - %s" % lines)

    points = {}

    for line in lines:
        start = [int(n) for n in line[0].split(",")]
        end = [int(n) for n in line[1].split(",")]

        if start[0] != end[0] and start[1] != end[1]:
            continue

        print("start - %s" % start)
        print("end - %s" % end)

        d = 1 if start[0] < end[0] else -1

        if start[1] != end[1]:
            d = 1 if start[1] < end[1] else -1

        for x in range(start[0], end[0]+d, d):
            for y in range(start[1], end[1]+d, d):
                hash_ = "%s,%s" % (x, y)
                print("marking - %s,%s" % (x, y))

                print("value = %s" % hash_ in points)

                points[hash_] = points.get(hash_, 0) + 1

    for point in points:
        print(points[point])

    return sum(1 if points[n] >= 2 else 0 for n in points)


# assert(problem('day.test') == 5)
# print(problem('day.in'))

def problem2(input):
    file = open(input, 'r')
    lines = [line.strip().split(" -> ") for line in file.readlines()]

    print("lines - %s" % lines)

    points = {}

    for line in lines:
        start = [int(n) for n in line[0].split(",")]
        end = [int(n) for n in line[1].split(",")]

        # if start[0] != end[0] and start[1] != end[1]:
        #     continue

        print("start - %s" % start)
        print("end - %s" % end)

        dx = (end[0] - start[0])
        dy = (end[1] - start[1])

        dx = 0 if dx == 0 else int(dx / abs(dx))
        dy = 0 if dy == 0 else int(dy / abs(dy))

        x = start[0]
        y = start[1]

        print("dx,dy - %s,%s" % (dx,dy))

        while True:
                hash_ = "%s,%s" % (x, y)
                print("marking - %s,%s" % (x, y))

                points[hash_] = points.get(hash_, 0) + 1

                if x == end[0] and y == end[1]:
                    break

                x += dx
                y += dy

    for point in points:
        print(points[point])

    return sum(1 if points[n] >= 2 else 0 for n in points)


assert(problem2('day.test') == 12)
print(problem2('day.in'))
