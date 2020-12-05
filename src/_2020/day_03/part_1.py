def run(lines):
    """
    198
    """
    results = 0
    position = 3
    for index, line in enumerate(lines):
        if index != 0:
            if position > len(line):
                while len(line) < position:
                    line += line
            if line[position] == '#':
                results += 1
            position += 3

    return results
