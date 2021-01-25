from . import THREE


def run(lines):
    """
    198
    """
    results = 0
    position = 3
    for line in lines[1::]:
        index = position % len(line)
        if line[index] == THREE:
            results += 1
        position += 3

    return results
