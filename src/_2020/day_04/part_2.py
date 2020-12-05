from . import validators, REQUIRED_FIELDS


def run(input_lines):
    """
    175
    """
    sorted_required_fields = sorted(REQUIRED_FIELDS)
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

            if sorted(passport.keys()) == sorted_required_fields:
                valid_passports += 1

            temp = {}

    return valid_passports
