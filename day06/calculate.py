import string


def getInput(file):
    with open(file) as f:
        lines = [l.rstrip("\n") for l in f.read().split("\n\n")]

    return lines


def calculate(file, part_b=False):
    groups = getInput(file)

    y_questions = 0
    for group in groups:
        alpha = set(string.ascii_lowercase)

        if not part_b:
            group_answers = set()
            for answer in group:
                if answer in alpha:
                    group_answers.add(answer)

            y_questions += group_answers.__len__()

        if part_b:
            group_members = len(group.split("\n"))
            group_answers = {}
            for person in group.split('\n'):
                for answer in person:
                    if not answer in group_answers:
                        group_answers[answer] = 1
                    else:
                        group_answers[answer] += 1

            print(group_answers)
            for answer, count in group_answers.items():
                if count == group_members:
                    y_questions += 1

    return y_questions


def getUniqueKeys(dict):
    result = set()
    for key in dict:
        result.add(key)
    return result


print(10*"-" + " AoC Day 6 " + 10*"-")
print("Test 1: " + str(calculate("test_input.txt")))
print("Output 1: " + str(calculate("input.txt")))
print("Test 2: " + str(calculate("test_input.txt", True)))
print("Output 2: " + str(calculate("input.txt", True)))
