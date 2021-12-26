def problem(input, steps):
    file = open(input, 'r')
    points = set([line.strip() for line in file.readlines() if "," in line])
    file = open(input, 'r')
    folds = [line.strip().replace("fold along ", "").split("=") for line in file.readlines() if "fold" in line]

    print("points - %s" % points)
    print("folds - %s" % folds)

    for step in range(0, steps):
        fold_axis = folds[step][0]
        fold_coord = int(folds[step][1])
        new_points = set()

        print("fold - (%s,%s)" % (fold_axis,fold_coord))

        for point in points:
            x = int(point.split(",")[0])
            y = int(point.split(",")[1])

            if fold_axis == "x":
                if x < fold_coord:
                    new_x = fold_coord - 1 - x

                    new_points.add("%s,%s" % (new_x, y))

                    print("folding - (%s,%s) along (%s,%s) to (%s,%s)" % (x, y, fold_axis, fold_coord, new_x, y))
                elif x > fold_coord:
                    print("moving - (%s,%s) along (%s,%s) to (%s,%s)" % (x, y, fold_axis, fold_coord, x - 1 - fold_coord, y))
                    new_points.add("%s,%s" % (x - 1 - fold_coord, y))
            else:
                if y > fold_coord:
                    new_y = fold_coord - (y - fold_coord)

                    new_points.add("%s,%s" % (x, new_y))

                    print("folding - (%s,%s) along (%s,%s) to (%s,%s)" % (x, y, fold_axis, fold_coord, x, new_y))
                elif y < fold_coord:
                    new_points.add("%s,%s" % (x, y))

        points = new_points

    print("sum - %s" % len(points))

    min_x = min(int(point.split(",")[0]) for point in points)
    max_x = max(int(point.split(",")[0]) for point in points)
    min_y = min(int(point.split(",")[1]) for point in points)
    max_y = max(int(point.split(",")[1]) for point in points)

    for y in range(min_y, max_y + 1):
        print("".join([("#" if "%s,%s" % (x, y) in points else ".") for x in range(min_x, max_x + 1)]))

    return len(points)


assert (problem('day.test', 1) == 17)

print(problem('day.in', 12))
