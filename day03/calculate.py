def getInput(file):
    lines = []
    with open(file) as f:
        ls = f.readlines()
        lines.extend([l.strip() for l in ls])

    return lines


def navigate(file, steps_right=3, steps_down=1):

    rows = getInput(file)
    row_length = rows[0].__len__()

    cur_x = 0
    cur_y = 0
    tree_count = 0

    while cur_y < rows.__len__():
        # check if the current tile is a tree, repeating the X
        if rows[cur_y][cur_x % row_length] == '#':
            tree_count += 1

        # Move
        cur_y += steps_down
        cur_x += steps_right

    return tree_count


def navigate_slopes(file):

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    trees = 1
    for steps_right, steps_down in slopes:
        trees *= navigate(file, steps_right, steps_down)

    return trees


print(10*"-" + " AoC Day 3 " + 10*"-")
print("Test 1: " + str(navigate("test_input.txt")))
print("Output 1: " + str(navigate("input.txt")))
print("Test 2: " + str(navigate_slopes("test_input.txt")))
print("Output 2: " + str(navigate_slopes("input.txt")))
