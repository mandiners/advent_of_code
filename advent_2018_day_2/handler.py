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


def find_common_words(input_data):
    """
    Advent of code 2018 II/2
    """
    words = []
    result = []
    max_len = len(input_data[0])
    for target_word in input_data:
        for word in input_data:
            matches = 0
            for index in range(max_len):
                if target_word[index] == word[index]:
                    matches += 1
            if max_len - matches == 1:
                words.append(target_word)

    if len(words) >= 2:
        checker = words[1]
        for index, letter in enumerate(words[0]):
            if letter == checker[index]:
                result.append(letter)

    return ''.join(result)
