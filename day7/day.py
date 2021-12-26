import math


def problem(input):
    file = open(input, 'r')
    positions = [int(position) for position in file.readline().split(",")]

    targets = set(positions)
    targets_dist = {}

    for target in targets:
        targets_dist[target] = sum(abs(position - target) for position in positions)

    min_ = min(targets_dist.values())

    print("min - %s" % min_)

    return min_

def problem2(input):
    file = open(input, 'r')
    positions = [int(position) for position in file.readline().split(",")]
    min_pos = min(positions)
    max_pos = max(positions)

    targets_dist = {}

    for target in range(min_pos, max_pos+1):
        targets_dist[target] = sum((abs(position - target) * (abs(position - target) + 1))/2 for position in positions)

    min_ = min(targets_dist.values())

    print("min - %s" % min_)

    return min_


assert(problem('day.test') == 37)

print(problem('day.in'))

assert(problem2('day.test') == 168)

print(problem2('day.in'))