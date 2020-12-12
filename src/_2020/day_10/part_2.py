from collections import defaultdict


def run(input_lines):
    """
    259172170858496
    """
    adapters = sorted([int(value) for value in input_lines])

    adapters.insert(0, 0)
    adapters.append(max(adapters) + 3)

    paths = defaultdict(int)

    for i, adapter in enumerate(adapters):
        for j in reversed(range(i)):
            if adapter - adapters[j] > 3:
                break
            paths[i] += paths[j] if j != 0 else 1

    return list(paths.values())[-1]
