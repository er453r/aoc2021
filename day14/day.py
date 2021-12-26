def problem(input, steps):
    file = open(input, 'r')
    base = file.readline().strip()
    inserts = {line.strip().split(" -> ")[0]:line.strip().split(" -> ")[1] for line in file.readlines() if "->" in line}

    pairs = {}

    for n in range(0, len(base) - 1):
        pair = f"{base[n]}{base[n+1]}"

        if pair in pairs:
            pairs[pair] += 1
        else:
            pairs[pair] = 1

    letter_counts = {}

    for letter in base:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

    print("pairs - %s" % pairs)
    print("base - %s" % base)
    print("inserts - %s" % inserts)
    print("letter_counts - %s" % letter_counts)

    for step in range(1, steps+1):
        print("STEP - %s" % step)
        # print("pairs - %s" % pairs)

        new_pairs = {}

        for pair in pairs:
            insert = inserts[pair]

            if insert in letter_counts:
                letter_counts[insert] += pairs[pair]
            else:
                letter_counts[insert] = pairs[pair]

            new_pair1 = f"{pair[0]}{insert}"
            new_pair2 = f"{insert}{pair[1]}"

            if new_pair1 in new_pairs:
                new_pairs[new_pair1] += pairs[pair]
            else:
                new_pairs[new_pair1] = pairs[pair]

            if new_pair2 in new_pairs:
                new_pairs[new_pair2] += pairs[pair]
            else:
                new_pairs[new_pair2] = pairs[pair]

        pairs = new_pairs

        print("letter_counts - %s" % letter_counts)
        print("len - %s" % sum(letter_counts[p] for p in letter_counts))

    print("pairs - %s" % pairs)

    print("letter_counts - %s" % letter_counts)

    counts = sorted(letter_counts.values())

    return counts.pop() - counts[0]


assert(problem('day.test', 10) == 1588)

print(problem('day.in', 10))

assert(problem('day.test', 40) == 2188189693529)

print(problem('day.in', 40))
