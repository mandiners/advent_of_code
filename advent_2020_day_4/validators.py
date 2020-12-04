import re


def byr_validator(value):
    return int(value) in range(1920, 2003)


def iyr_validator(value):
    return int(value) in range(2010, 2021)


def eyr_validator(value):
    return int(value) in range(2020, 2031)


def hgt_validator(value):
    if re.search("([a-z)])", value):
        height = int(value[:-2:])
        unit = value[-2::]
        if unit == 'cm':
            return height in range(150, 194)
        elif unit == 'in':
            return height in range(59, 77)

    return False


def hcl_validator(value):
    return re.fullmatch("(#[0-9a-f]{6})", value) is not None


def ecl_validator(value):
    return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def pid_validator(value):
    return re.fullmatch("([0-9]{9})", value) is not None
