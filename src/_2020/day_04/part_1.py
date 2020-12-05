from . import REQUIRED_FIELDS


def run(input_lines):
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
