def run(input_lines):
    """
    22477624
    """
    preambles = [int(value) for value in input_lines]

    for index, value in enumerate(preambles, 1):
        if index > 25:
            temp = False
            threshold = preambles[:index - 1:]
            for i in threshold:
                for j in threshold:
                    if i + j == value:
                        temp = True
                        break

            if not temp:
                return value
