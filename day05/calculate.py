def getInput(file):
    lines = []
    with open(file) as f:
        ls = f.readlines()
        lines.extend([l.strip() for l in ls])
    return lines


def calculate(file, b=False):
    lines = getInput(file)
    max = 0
    coll = set()

    map = {
        "F": "0",
        "B": "1",
        "L": "0",
        "R": "1"
    }

    for line in lines:
        for a, b in map.items():
            line = line.replace(a, b)
        num = int(line, 2)
        coll.add(num)
        max = max(num, max)
    

    if b:
        for i in range(256 * 8):
            if i not in coll and i+1 in coll and i-1 in coll:
                return i
    return max


print(10*"-" + " AoC Day 5 " + 10*"-")
print("Test 1: " + str(calculate("test_input.txt")))
print("Output 1: " + str(calculate("input.txt")))
print("Test 2: " + str(calculate("test_input.txt", True)))
print("Output 2: " + str(calculate("input.txt", True)))
