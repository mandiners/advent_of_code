import datetime as dt
from utils.parser import input_parser, formatter
from advent_2018_day_1.handler import calculator, add
from advent_2018_day_2.handler import check_sum_counter, find_common_words
from advent_2018_day_3.handler import overlap_checker, overlap_checker_2
from advent_2020_day_1.handler import find_two_values_to_sum_2020_and_multiplying,\
    find_three_values_to_sum_2020_and_multiplying
from advent_2020_day_2.handler import password_validator, super_password_validator
from advent_2020_day_3.handler import tree_counter, tree_counter2
from advent_2020_day_4.handler import passport_validator, passport_validator2

if __name__ == '__main__':
    # Start Timer
    start_time = dt.datetime.now()

    # Parsing
    raw_data = input_parser('advent_2020_day_4/input.txt')
    data = formatter(raw_data)

    # Run
    result = passport_validator2(data)

    # End of Task
    print(f"Run time: {dt.datetime.now() - start_time}")
    print(f"Result: {result}")
