from . import ACC, JMP, NOP


def run_command(commands, index=0, accumulator=0):
    if index < len(commands.keys()):
        command = commands[index]
        command['seen'] += 1

        if command['seen'] < 2:
            if command['operation'] == NOP:
                return run_command(commands, index + 1, accumulator)
            elif command['operation'] == JMP:
                index += command['value']
                return run_command(commands, index, accumulator)
            elif command['operation'] == ACC:
                accumulator += command['value']
                return run_command(commands, index + 1, accumulator)
    else:
        return accumulator


def run(input_lines):
    """
    1036
    """

    operations = [i.split(' ') for i in input_lines]

    for index, line in enumerate(input_lines):
        if not any(x in line for x in ["0", ACC]):
            temp = {}
            for i, v in enumerate(operations):
                operation, value = v[0], int(v[1])
                if index == i:
                    operation = JMP if operation == NOP else NOP
                temp[i] = {'operation': operation, 'value': value, 'seen': 0}

            accumulator = run_command(temp)
            if accumulator:
                return accumulator
