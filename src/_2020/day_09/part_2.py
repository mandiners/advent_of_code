def run(input_lines):
    """
    2980044
    """
    target_number = 22477624
    preambles = [int(value) for value in input_lines]

    for index, value in enumerate(preambles):
        temp = value
        contiguous_set = [temp]
        for i in preambles[index + 1::]:
            temp += i
            contiguous_set.append(i)
            if temp == target_number:
                return min(contiguous_set) + max(contiguous_set)
            elif temp > target_number:
                break
