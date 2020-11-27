from _collections import defaultdict


def check_sum_counter(input_data):
    """
    Advent of code 2018 II/1
    """
    results = []
    for word in input_data:
        temp = defaultdict(int)
        for letter in word:
            temp[letter] += 1
        results.append(set([i for i in temp.values() if i > 1]))

    contain_two = len(results)
    contain_three = len([i for i in results if len(i) > 1])
    return contain_two * contain_three
