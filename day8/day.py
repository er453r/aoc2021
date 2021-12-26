def problem(input):
    file = open(input, 'r')
    readouts = [line.split(" | ")[1].split() for line in file.readlines()]

    print("readouts - %s" % readouts)

    unique_readouts = list()

    [[unique_readouts.append(readout) for readout in readout_series if len(readout) in [2, 3, 4, 7]] for readout_series in readouts]

    return len(unique_readouts)


# assert (problem('day.test') == 26)
#
# print(problem('day.in'))


def problem2(input):
    file = open(input, 'r')
    all = [line.split(" | ")[0].split() for line in file.readlines()]
    file = open(input, 'r')
    readouts = [line.split(" | ")[1].split() for line in file.readlines()]

    print("readouts - %s" % readouts)

    print("all - %s" % len(all))
    print("readouts - %s" % len(readouts))

    sum = 0

    for index, unique in enumerate(all):
        key = {
            1: [set(u) for u in unique if len(u) == 2][0],
            4: [set(u) for u in unique if len(u) == 4][0],
            7: [set(u) for u in unique if len(u) == 3][0],
            8: set("abcdefg")
        }

        uL = key[4].difference(key[1])
        dL = key[8].difference(key[7]).difference(uL)

        print("uL - %s" % uL)
        print("dL - %s" % dL)

        elem5 = [set(u) for u in unique if len(u) == 5]
        print("elem5 - %s" % elem5)

        two = next(e for e in elem5 if e.issuperset(dL))
        five = next(e for e in elem5 if e.issuperset(uL))
        elem5.remove(two)
        elem5.remove(five)
        three = elem5[0]

        print("two - %s" % two)
        print("three - %s" % three)
        print("five - %s" % five)

        elem6 = [set(u) for u in unique if len(u) == 6]
        print("elem6 - %s" % elem6)

        six = next(e for e in elem6 if e.issuperset(dL) and e.issuperset(uL))
        elem6.remove(six)
        nine = next(e for e in elem6 if e.issuperset(uL))
        elem6.remove(nine)
        zero = elem6[0]

        print("six - %s" % six)
        print("nine - %s" % nine)
        print("zero - %s" % zero)

        decode = {
            "".join(sorted(zero)): 0,
            "".join(sorted(key[1])): 1,
            "".join(sorted(two)): 2,
            "".join(sorted(three)): 3,
            "".join(sorted(key[4])): 4,
            "".join(sorted(five)): 5,
            "".join(sorted(six)): 6,
            "".join(sorted(key[7])): 7,
            "".join(sorted(key[8])): 8,
            "".join(sorted(nine)): 9,
        }

        print("decode - %s" % decode)
        sorted_readouts = ["".join(sorted(readout)) for readout in readouts[index]]

        print("sorted_readouts - %s" % sorted_readouts)

        value = 1000 * decode[sorted_readouts[0]] + 100 * decode[sorted_readouts[1]] + 10 * decode[sorted_readouts[2]] + decode[sorted_readouts[3]]

        print("value - %s" % value)

        sum += value

    return sum


assert (problem2('day.test') == 61229)

print(problem2('day.in'))