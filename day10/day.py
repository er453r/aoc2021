def problem(input):
    file = open(input, 'r')
    lines = [line.strip() for line in file.readlines()]

    closers = {
        '}': '{',
        ')': '(',
        ']': '[',
        '>': '<',
    }

    score = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }

    total = 0

    for line in lines:
        stack = []

        for char in line:
            if char in closers:
                if len(stack) == 0 or stack.pop() != closers[char]:
                    print("error - %s" % char)

                    total += score[char]

                    break
            else:
                stack.append(char)

                print("stack - %s" % stack)

    print("total - %s" % total)

    return total


# assert (problem('day.test') == 26397)
#
# print(problem('day.in'))

def problem2(input):
    file = open(input, 'r')
    lines = [line.strip() for line in file.readlines()]

    closers = {
        '}': '{',
        ')': '(',
        ']': '[',
        '>': '<',
    }

    openers = {
        '{': '}',
        '(': ')',
        '[': ']',
        '<': '>',
    }

    scores = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }

    total = []

    for line in lines:
        stack = []
        error = False
        score = 0

        for char in line:
            if char in closers:
                if len(stack) == 0 or stack.pop() != closers[char]:
                    error = True

                    break
            else:
                stack.append(char)

        if not error:
            print("stack - %s" % stack)

            while len(stack) > 0:
                top = stack.pop()

                score = score * 5 + scores[openers[top]]

            print(score)

            total.append(score)

    print("total - %s" % total)

    total = sorted(total)

    return total[int(len(total)/2)]


assert (problem2('day.test') == 288957)

print(problem2('day.in'))
