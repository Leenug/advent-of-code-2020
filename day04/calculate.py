import re


def getInput(file):
    with open(file) as f:
        return f.readlines()


def tryInt(str):
    if(str[0] == '0'):
        return str
    try:
        return int(str)
    except ValueError:
        return str


def validate(file, do_validation=False):

    rows = getInput(file)
    valid_passports = 0

    required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    passports = ""
    for row in rows:
        passports += row

    for passport in passports.split("\n\n"):
        valid = False
        data = getPassportData(passport)

        all_required_keys = all(key in data for key in required_keys)

        if all_required_keys:
            if do_validation:
                valid = all(validate_key(key, data[key])
                            for key in required_keys)
            else:
                valid = True

        valid_passports += valid

    return valid_passports


def validate_key(key, value):
    if key == 'hgt':
        try:
            if value[-2:] == 'cm':
                return int(value[:-2]) >= 150 and int(value[:-2]) <= 193
            if value[-2:] == 'in':
                return int(value[:-2]) >= 59 and int(value[:-2]) <= 76
        except (ValueError, TypeError):
            return False

    if key == 'byr':
        return isinstance(value, int) and value >= 1920 and value <= 2002

    if key == 'iyr':
        return isinstance(value, int) and value >= 2010 and value <= 2020

    if key == 'eyr':
        return isinstance(value, int) and value >= 2020 and value <= 2030

    if key == 'hcl':
        valid_chars = '0123456789abcdef'
        return isinstance(value, str) and len(value) == 7 and value[0] == '#' and all(c in valid_chars for c in value[1:])

    if key == 'ecl':
        valid_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        return isinstance(value, str) and value in valid_colors

    if key == 'pid':
        value = str(value)
        try:
            return len(value) == 9 and all(isinstance(int(x), int) for x in value)
        except ValueError:
            return False


def getPassportData(passport):

    pairs = re.split("\\s", passport)

    data = {}
    for pair in pairs:
        key, value = pair.split(":")
        data[key] = tryInt(value)

    return data


print(10*"-" + " AoC Day 4 " + 10*"-")
print("Test 1: " + str(validate("test_input.txt")))
print("Output 1: " + str(validate("input.txt")))
print("Test 2 (invalid): " + str(validate("test_2_invalid.txt", True)))
print("Test 2 (valid): " + str(validate("test_2_valid.txt", True)))
print("Output 2: " + str(validate("input.txt", True)))
