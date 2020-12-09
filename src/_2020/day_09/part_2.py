TARGET_NUMBER = 22477624


def run(input_lines):
    """
    2980044
    """
    preambles = [int(value) for value in input_lines]

    for index, value in enumerate(preambles):
        sequence_list = [value]
        sum_of_seq = value

        for preamble in preambles[index + 1::]:
            sum_of_seq += preamble
            sequence_list.append(preamble)

            if sum_of_seq == TARGET_NUMBER:
                return min(sequence_list) + max(sequence_list)
            elif sum_of_seq > TARGET_NUMBER:
                break
