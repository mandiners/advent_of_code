def add(numbers):
    """
    Advent of code 2018 I/1
    """
    total = 0
    for number in numbers:
        total += int(number)

    return total


def calculator(numbers):
    """
    Advent of code 2018 I/2
    """
    total = 0
    freq_history = set()
    result = None

    while result is None:
        for outer in numbers:
            for inner in numbers:
                total += int(inner)
                prev_list_len = len(freq_history)
                freq_history.add(total)
                if prev_list_len == len(freq_history):
                    result = total
                    break
            if result:
                break

    return result
