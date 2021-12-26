def problem(input, days):
    file = open(input, 'r')
    ages = [int(age) for age in file.readline().split(",")]

    print("ages - %s" % ages)

    state = {}

    for timer in range(0, 9):
        state[timer] = sum(1 if age == timer else 0 for age in ages)

    print("state - %s" % state)

    for _ in range(0, days):
        next_state = {}

        for timer in range(0, 8):
            next_state[timer] = state[timer+1]

        next_state[8] = state[0]
        next_state[6] += state[0]
        # print("next_state - %s" % next_state)

        state = next_state

    return sum(state[age] for age in state)


assert(problem('day.test', 18) == 26)
assert(problem('day.test', 80) == 5934)

print(problem('day.in', 80))

assert(problem('day.test', 256) == 26984457539)

print(problem('day.in', 256))
