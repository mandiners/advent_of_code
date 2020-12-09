SEQUENCE_LEN = 25


def run(input_lines):
    """
    22477624
    """
    preambles = [int(value) for value in input_lines]

    for index, preamble in enumerate(preambles[SEQUENCE_LEN::]):
        counter = 0
        index += SEQUENCE_LEN
        target_sequence = preambles[index - SEQUENCE_LEN:index:]

        for i in target_sequence:
            counter += 1
            for j in target_sequence:
                if i + j == preamble:
                    counter = 0
                    break

        if counter == SEQUENCE_LEN:
            return preamble
