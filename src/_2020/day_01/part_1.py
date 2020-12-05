def run(input_data):
    """
    618144
    """
    numbers = [int(i) for i in input_data]
    for i in range(len(numbers)):
        ni = numbers[i]
        for j in range(i + 1, len(numbers)):
            nj = numbers[j]
            if ni + nj == 2020:
                return ni * nj
