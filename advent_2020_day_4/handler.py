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
    fields = set()
    lines = input_lines if input_lines[-1] is None else [*input_lines, *[None]]

    for line in lines:
        if line:
            data = line.split(' ')
            for field in data:
                fields.add(field.split(':')[0])
        else:
            fields = [i for i in fields if i != 'cid']
            if sorted(fields) == sorted(REQUIRED_FIELDS):
                valid_passports += 1
            fields = set()

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
                key, value = field.split(':')
                if key != 'cid':
                    temp[key] = value
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
