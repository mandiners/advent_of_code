def run(input_lines):
    """
    3034
    """
    adapters = sorted([int(value) for value in input_lines])

    adapters.insert(0, 0)
    adapters.append(max(adapters) + 3)

    one_differences, three_differences = 0, 0

    for index, adapter in enumerate(adapters):
        previous_adapter = adapters[index - 1]

        if adapter - previous_adapter == 1:
            one_differences += 1
        elif adapter - previous_adapter == 3:
            three_differences += 1

    return one_differences * three_differences
