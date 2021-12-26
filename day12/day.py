def visit(node, paths, forbidden={"start"}):
    print("visiting - %s" % node)

    if node == 'end':
        return 1

    if node.islower():
        forbidden.add(node)

    paths_found = 0

    for next_ in paths[node]:
        if next_ in forbidden:
            continue

        print("going %s -> %s" % (node, next_))

        paths_found += visit(next_, paths, forbidden.copy())

    return paths_found


def problem(input):
    file = open(input, 'r')
    paths_ = [line.strip().split("-") for line in file.readlines()]

    paths = {}

    for path_ in paths_:
        if path_[0] in paths:
            paths[path_[0]].add(path_[1])
        else:
            paths[path_[0]] = set([path_[1]])

        if path_[1] in paths:
            paths[path_[1]].add(path_[0])
        else:
            paths[path_[1]] = set([path_[0]])

    print("paths - %s" % paths)

    sum_ = visit('start', paths)

    print("sum - %s" % sum_)

    return sum_


# assert (problem('day.test') == 10)
#
# print(problem('day.in'))

def visit2(node, paths, forbidden={"start"}, exception_used=False, path=""):
    print("visiting - %s" % node)

    path += "%s-" % node

    if node == 'end':
        return [path]

    paths_found = []
    forbidden_wo_exc = forbidden.copy()

    if node.islower() and node != "start":
        forbidden.add(node)

        if not exception_used:
            print("using exception for %s" % node)

            for next_ in paths[node]:
                if next_ in forbidden_wo_exc:
                    continue

                print("going %s -> %s" % (node, next_))

                paths_found.extend(visit2(next_, paths, forbidden_wo_exc.copy(), True, path))

    for next_ in paths[node]:
        if next_ in forbidden:
            continue

        print("going %s -> %s" % (node, next_))

        paths_found.extend(visit2(next_, paths, forbidden.copy(), exception_used, path))

    return paths_found


def problem2(input):
    file = open(input, 'r')
    paths_ = [line.strip().split("-") for line in file.readlines()]

    paths = {}

    for path_ in paths_:
        if path_[0] in paths:
            paths[path_[0]].add(path_[1])
        else:
            paths[path_[0]] = set([path_[1]])

        if path_[1] in paths:
            paths[path_[1]].add(path_[0])
        else:
            paths[path_[1]] = set([path_[0]])

    print("paths - %s" % paths)

    paths_found = visit2('start', paths)
    paths_found = set(paths_found)

    print("paths_found - %s" % len(paths_found))

    return len(paths_found)


assert (problem2('day.test') == 36)

print(problem2('day.in'))
