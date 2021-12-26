def problem(input):
    file = open(input, 'r')
    lines = [line.strip() for line in file.readlines()]

    numbers = [int(n) for n in lines[0].split(",")]

    number_of_boards = int((len(lines) - 1) / 6)
    boards = []

    for b in range(2, len(lines), 6):
        rows = [lines[b + r].split() for r in range(0, 5)]
        columns = [[row[c] for row in rows] for c in range(0, 5)]

        for index, row in enumerate(rows):
            rows[index] = [int(n) for n in row]

        for index, column in enumerate(columns):
            columns[index] = [int(n) for n in column]

        boards.append(dict(
            id=int((b-2)/6)+1,
            rows=[set(row) for row in rows],
            columns=[set(column) for column in columns],
        ))

    print("number_of_boards - %s" % number_of_boards)
    print("numbers - %s" % numbers)
    print("boards - %s" % boards)

    for number in numbers:
        print("number - %s" % number)

        for board in boards:
            for row in board['rows']:
                row.discard(number)

                print(len(row))

                if len(row) == 0:
                    print("winning board - %s row %s" % (board, row))

                    sum_ = sum([sum(row) for row in board['rows']])

                    print("winning board sum - %s" % sum_)
                    print("winning board number - %s" % number)
                    print("winning board result - %s" % (sum_ * number))

                    return sum_ * number

            for column in board['columns']:
                column.discard(number)
                print(len(column))
                if len(column) == 0:
                    print("winning board - %s for column %s" % (board, column))

                    sum_ = sum([sum(column) for column in board['columns']])

                    print("winning board sum - %s" % sum_)
                    print("winning board number - %s" % number)
                    print("winning board result - %s" % (sum_ * number))

                    return sum_ * number

        print("all numbers...")


# assert(problem('day4.test') == 4512)
# print(problem('day4.in'))


def problem2(input):
    file = open(input, 'r')
    lines = [line.strip() for line in file.readlines()]

    numbers = [int(n) for n in lines[0].split(",")]

    number_of_boards = int((len(lines) - 1) / 6)
    boards = []

    for b in range(2, len(lines), 6):
        rows = [lines[b + r].split() for r in range(0, 5)]
        columns = [[row[c] for row in rows] for c in range(0, 5)]

        for index, row in enumerate(rows):
            rows[index] = [int(n) for n in row]

        for index, column in enumerate(columns):
            columns[index] = [int(n) for n in column]

        boards.append(dict(
            won=False,
            id=int((b-2)/6)+1,
            rows=[set(row) for row in rows],
            columns=[set(column) for column in columns],
        ))

    print("number_of_boards - %s" % number_of_boards)
    print("numbers - %s" % numbers)
    print("boards - %s" % boards)

    for number in numbers:
        print("number - %s" % number)

        for board in boards:
            for row in board['rows']:
                if number in row:
                    print("board %s - mark %s in row" % (board['id'], number))

                row.discard(number)

                if len(row) == 0:
                    board['won'] = True

                    print("winning board - %s row %s" % (board, row))

                    sum_ = sum([sum(row) for row in board['rows']])

                    print("winning board sum - %s" % sum_)
                    print("winning board number - %s" % number)
                    print("winning board result - %s" % (sum_ * number))
                    print("boards left - %s" % len(boards))

                    if sum([1 if b['won'] else 0 for b in boards]) == len(boards):
                        return sum_ * number

            for column in board['columns']:
                if number in column:
                    print("board %s - mark %s in column" % (board['id'], number))

                column.discard(number)

                if len(column) == 0:
                    board['won'] = True

                    print("winning board - %s for column %s" % (board, column))

                    sum_ = sum([sum(column) for column in board['columns']])

                    print("winning board sum - %s" % sum_)
                    print("winning board number - %s" % number)
                    print("winning board result - %s" % (sum_ * number))
                    print("boards left - %s" % len(boards))

                    if sum([1 if b['won'] else 0 for b in boards]) == len(boards):
                        return sum_ * number

    print("all numbers...")

assert(problem2('day4.test') == 1924)
print(problem2('day4.in'))
