from . import validators

REQUIRED_FIELDS = (
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
    )


def passport_validator(input_lines):
    """
    228
    """
    valid_passports = 0
    temp = set()
    lines = input_lines if input_lines[-1] is None else [*input_lines, *[None]]

    for line in lines:
        if line:
            fields = line.split(' ')
            for field in fields:
                field_name = field.split(':')[0]
                if field_name != 'cid':
                    temp.add(field_name)
        else:
            if len(temp) == len(REQUIRED_FIELDS):
                valid_passports += 1
            temp = set()

    return valid_passports


def passport_validator2(input_lines):
    """
    175
    """
    valid_passports = 0
    temp = {}
    lines = input_lines if input_lines[-1] is None else [*input_lines, *[None]]

    for line in lines:
        if line:
            fields = line.split(' ')
            for field in fields:
                field_name, value = field.split(':')
                if field_name != 'cid':
                    temp[field_name] = value
        else:
            passport = {}
            for field_name, value in temp.items():
                if validator := getattr(validators, f'{field_name}_validator'):
                    if is_valid := validator(value):
                        passport[field_name] = is_valid

            if len(passport.keys()) == len(REQUIRED_FIELDS):
                valid_passports += 1

            temp = {}

    return valid_passports
