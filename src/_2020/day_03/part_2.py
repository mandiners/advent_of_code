def run(lines):
    """
    5140884672
    """
    slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    tree_list = []
    for slope in slopes:
        result = 0
        right, down = slope
        position = right
        for index, line in enumerate(lines):
            if index != 0 and index % down == 0:
                if position >= len(line):
                    while len(line) <= position:
                        line += line
                if line[position] == '#':
                    result += 1
                position += right

        tree_list.append(result)

    results = 1
    for i in tree_list:
        results = results * i

    return results
