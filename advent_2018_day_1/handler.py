def add(numbers):
    """
    Advent of code 2018 I/1
    """
    total = 0
    for number in numbers:
        total += int(number)

    return total


def calculator(input_list):
    """
    Advent of code 2018 I/2
    """
    numbers = [int(i) for i in input_list]
    total = 0
    freq_history = set()

    for loop_counter in numbers:
        for number in numbers:
            total += number
            prev_list_len = len(freq_history)
            freq_history.add(total)
            if prev_list_len == len(freq_history):
                return total
