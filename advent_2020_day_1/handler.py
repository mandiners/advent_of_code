def find_two_values_to_sum_2020_and_multiplying(input_data):
    numbers = [int(i) for i in input_data]
    for i in range(len(numbers)):
        ni = numbers[i]
        for j in range(i + 1, len(numbers)):
            nj = numbers[j]
            if ni + nj == 2020:
                return ni * nj


def find_three_values_to_sum_2020_and_multiplying(input_data):
    numbers = [int(i) for i in input_data]
    for i in range(len(numbers)):
        ni = numbers[i]
        for j in range(i + 1, len(numbers)):
            nj = numbers[j]
            if ni + nj >= 2000:
                continue
            else:
                for k in range(j + 1, len(numbers)):
                    nk = numbers[k]
                    if ni + nj + nk == 2020:
                        return ni * nj * nk
