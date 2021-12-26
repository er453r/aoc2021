import heapq
import math


def problem(input_, full=False):
    file = open(input_, 'r')
    readouts = [[int(i) for i in list(line.strip())] for line in file.readlines()]

    width = len(readouts[0])
    height = len(readouts)

    print("width - %s" % width)
    print("height - %s" % height)

    if full:
        full_map = [[(readouts[y % height][x % width] - 1 + math.floor(x / width) + math.floor(y / height)) % 9 + 1 for y in range(0, width * 5)] for x in range(0, height * 5)]

        readouts = full_map

        # print(full_map)

        width = len(readouts[0])
        height = len(readouts)

        print("width - %s" % width)
        print("height - %s" % height)

    source = (0, 0)
    target = (width - 1, height - 1)
    vertices = [(x, y) for x in range(0, width) for y in range(0, height)]
    values = {v: readouts[v[1]][v[0]] for v in vertices}

    queue = set()
    heap_queue = []
    distances = {}
    costs = {}
    previous = {}

    for vertex in vertices:
        distances[vertex] = 10e15
        costs[vertex] = 10e15
        previous[vertex] = None
        heapq.heappush(heap_queue, (distances[vertex], vertex))
        queue.add(vertex)

    distances[source] = 0
    costs[source] = 0

    # print("distances - %s" % distances)

    while len(heap_queue) > 0:
        min_costs_vertex = heapq.heappop(heap_queue)[1]
        queue.remove(min_costs_vertex)

        if min_costs_vertex == target:
            print("found it!")

            break

        for neighbour in [
            (min_costs_vertex[0] - 1, min_costs_vertex[1] + 0),
            (min_costs_vertex[0] + 1, min_costs_vertex[1] + 0),
            (min_costs_vertex[0] + 0, min_costs_vertex[1] - 1),
            (min_costs_vertex[0] + 0, min_costs_vertex[1] + 1),
        ]:
            if neighbour not in queue:
                continue

            # math.sqrt((neighbour[0] - target[0]) ** 2 + (neighbour[1] - target[1]) ** 2)
            alternative_cost = distances[min_costs_vertex] + values[neighbour]
            alternative_distance = distances[min_costs_vertex] + values[neighbour]

            if alternative_cost < costs[neighbour]:
                costs[neighbour] = alternative_cost
                distances[neighbour] = alternative_distance
                previous[neighbour] = min_costs_vertex

                heapq.heappush(heap_queue, (alternative_distance, neighbour))

    print("distance from %s to %s - %s" % (source, target, distances[target]))

    return distances[target]


assert (problem('day.test') == 40)

print(problem('day.in'))

assert (problem('day.test', True) == 315)

print(problem('day.in', True))
