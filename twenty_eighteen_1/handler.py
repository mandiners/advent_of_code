def calculator(numbers):
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
