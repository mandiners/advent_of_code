import datetime as dt
from utils.parser import input_parser, formatter
from advent_2018_day_1.handler import calculator, add


if __name__ == '__main__':
    # Start Timer
    start_time = dt.datetime.now()

    # Parsing
    raw_data = input_parser('advent_2018_day_1/input.txt')
    data = formatter(raw_data)

    # Run
    result = calculator(data)

    # End of Task
    print(f"Run time: {dt.datetime.now() - start_time}")
    print(result)
