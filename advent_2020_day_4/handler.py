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


def passport_validator(lines):
    """
    228
    """
    valid_passports = 0
    fields = []
    for line in lines:
        if line:
            data = line.split(' ')
            for field in data:
                fields.append(field.split(':')[0])
        else:
            fields = [i for i in fields if i != 'cid']
            if len(REQUIRED_FIELDS) == len(fields):
                valid_passports += 1
            fields = []

    return valid_passports


def passport_validator2(lines):
    """
    175
    """
    threshold = len(REQUIRED_FIELDS)
    valid_passports = 0
    data = {}

    for line in lines:
        if line:
            line = line.split(' ')
            for field in line:
                key, value = field.split(':')
                data[key] = value
        else:
            valid_fields = 0
            for key, value in data.items():
                if key == 'cid':
                    continue
                if validator := getattr(validators, f'{key}_validator'):
                    is_valid = validator(value)
                    if is_valid:
                        valid_fields += 1
            if valid_fields == threshold:
                valid_passports += 1
            data = {}

    return valid_passports
