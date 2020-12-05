def run(input_data):
    """
    ymdrchgpvwfloluktajxijsqb
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
