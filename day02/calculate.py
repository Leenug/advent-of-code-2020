import re


def is_valid(password, position_check):
    # match th epattern
    pattern = r"(?P<min_count>\d+)-(?P<max_count>\d+)[ ](?P<char>.):[ ](?P<password>.*)"
    match = re.match(pattern, password)

    # split into parts
    min_count = int(match.group("min_count"))
    max_count = int(match.group("max_count"))
    char = match.group("char").strip()
    password = match.group("password").strip()

    # part 2: check position of char instead of count
    if position_check:
        pos_checks = [
            password[min_count - 1],
            password[max_count - 1]
        ]

        if pos_checks.count(char) == 1:
            return True
    else:
        if password.count(char) in range(min_count, max_count + 1):
            return True

    return False


def getInput(file):
    lines = []
    with open(file) as f:
        ls = f.readlines()
        lines.extend([l.strip() for l in ls])

    return lines


def check(file, position_check=False):
    passwords = getInput(file)
    valid_count = 0
    for password in passwords:
        if is_valid(password, position_check):
            valid_count += 1

    return valid_count


print(10*"-" + " AoC Day 2 " + 10*"-")
print("Test 1: " + str(check("test_input.txt")))
print("Output 1: " + str(check("input.txt")))
print("Test 2: " + str(check("test_input.txt", True)))
print("Output 2: " + str(check("input.txt", True)))
