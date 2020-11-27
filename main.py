import datetime as dt
from utils.parser import input_parser, formatter
from advent_2018_day_1.handler import calculator, add
from advent_2018_day_2.handler import check_sum_counter, find_common_words


if __name__ == '__main__':
    # Start Timer
    start_time = dt.datetime.now()

    # Parsing
    raw_data = input_parser('advent_2018_day_2/input.txt')
    data = formatter(raw_data)

    # Run
    result = find_common_words(data)

    # End of Task
    print(f"Run time: {dt.datetime.now() - start_time}")
    print(result)
