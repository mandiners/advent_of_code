def find_two_values_to_sum_2020_and_multiplying(input_data):
    numbers = set([int(i) for i in input_data])
    for number in numbers:
        for possible_multiplier in numbers:
            if number + possible_multiplier == 2020:
                return number * possible_multiplier


def find_three_values_to_sum_2020_and_multiplying(input_data):
    numbers = set([int(i) for i in input_data])
    for number in numbers:
        for possible_first_multiplier in numbers:
            if possible_first_multiplier + number >= 2000:
                continue
            else:
                for possible_second_multiplier in numbers:
                    if number + possible_first_multiplier + possible_second_multiplier == 2020:
                        return number * possible_first_multiplier * possible_second_multiplier
