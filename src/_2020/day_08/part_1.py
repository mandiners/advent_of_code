from . import ACC, JMP, NOP


def run_commands(index, commands, accumulator=0):
    command = commands[index]
    command['seen'] += 1

    if command['seen'] < 2:
        if command['operation'] == NOP:
            return run_commands(index + 1, commands, accumulator)
        elif command['operation'] == JMP:
            index += command['value']
            return run_commands(index, commands, accumulator)
        elif command['operation'] == ACC:
            accumulator += command['value']
            return run_commands(index + 1, commands, accumulator)

    return accumulator


def run(input_lines):
    """
    1797
    """
    commands = {}

    for index, line in enumerate(input_lines):
        operation, value = line.split(' ')
        commands[index] = {'operation': operation,
                           'value': int(value),
                           'seen': 0}

    accumulator = run_commands(0, commands)

    return accumulator
