def run(input_list):
    """
    287
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
