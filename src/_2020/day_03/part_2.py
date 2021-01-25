from . import THREE
import functools


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
        for index, line in enumerate(lines[::down]):
            if index != 0:
                current_pos = position % len(line)
                if line[current_pos] == THREE:
                    result += 1
                position += right

        tree_list.append(result)

    return functools.reduce(lambda a, b: a * b, tree_list)
