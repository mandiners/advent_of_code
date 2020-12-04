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
    fields = set()
    lines = lines if lines[-1] is None else [*lines, *[None]]

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


def passport_validator2(lines):
    """
    175
    """
    valid_passports = 0
    data = {}
    lines = lines if lines[-1] is None else [*lines, *[None]]

    for line in lines:
        if line:
            fields = line.split(' ')
            for field in fields:
                key, value = field.split(':')
                if key != 'cid':
                    data[key] = value
        else:
            for field_name, value in data.items():
                if validator := getattr(validators, f'{field_name}_validator'):
                    data[field_name] = validator(value)

            field_list = set(i for i in data.keys())
            are_all_fields_are_valid = all(value for value in data.values())

            if are_all_fields_are_valid and sorted(field_list) == sorted(REQUIRED_FIELDS):
                valid_passports += 1

            data = {}

    return valid_passports
