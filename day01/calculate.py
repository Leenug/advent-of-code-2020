def calculate(file: str, target: int) -> int:
    """ Finds 2 numebrs that sum up to target and returns the product"""
    numbers = getFileLines(file)

    for a in range(numbers.__len__()):
        for b in range(numbers.__len__()):
            if a != b and numbers[a] + numbers[b] == target:
                return numbers[a] * numbers[b]


def calculate3(file: str, target: int) -> int:
    """ Finds 3 numebrs that sum up to target and returns the product"""
    numbers = getFileLines(file)

    for a in range(numbers.__len__()):
        for b in range(numbers.__len__()):
            for c in range(numbers.__len__()):
                if a != b and a != c and c != b:
                    if numbers[a] + numbers[b] + numbers[c] == target:
                        return numbers[a] * numbers[b] * numbers[c]


def getFileLines(file: str):
    with open(file, 'r') as f:
        lines = [int(l.replace("\n", "")) for l in f.readlines()]
    return lines


print(10*"-" + " AoC Day 1 " + 10*"-")
print("Test 1: " + str(calculate("test_input.txt", 2020)))
print("Output 1: " + str(calculate("input.txt", 2020)))
print("Test 2: " + str(calculate3("test_input.txt", 2020)))
print("Output 2: " + str(calculate3("input.txt", 2020)))
