import argparse
import datetime as dt
import importlib
import sys
from utils.parser import input_parser, formatter


def z_fill(day):
    return day.zfill(2)


def run(callback, input_path):
    # Start Timer
    start_time = dt.datetime.now()

    # Parsing
    raw_data = input_parser(input_path)
    data = formatter(raw_data)

    # Run
    result = callback.run(data)

    # End of Task
    print(f"Run time: {dt.datetime.now() - start_time}")
    print(f"Result: {result}")


if __name__ == '__main__':
    modulo = None
    parser = argparse.ArgumentParser(description='Advent of Code')
    parser.add_argument('year', type=str, help='Input year')
    parser.add_argument('day', type=z_fill, help='Input day')
    parser.add_argument('part', type=str, help='Input part')
    args = parser.parse_args()
    year, day, part = args.year, args.day, args.part
    try:
        year_module = importlib.import_module(f"src.{year}")
    except ModuleNotFoundError as e:
        print(f'Cannot import year({year}) module!')
        sys.exit()

    try:
        day_module = importlib.import_module(f"src.{year}.day_{day}")
    except ModuleNotFoundError as e:
        print(f'Cannot import year({year}) day({day}) module!')
        sys.exit()

    try:
        modulo = importlib.import_module(f"src.{year}.day_{day}.part_{part}")
    except ModuleNotFoundError as e:
        print(f'Cannot import year({year}) day({day}) part({part}) module!')
        sys.exit()

    if modulo:
        if hasattr(modulo, 'run'):
            input_path = f"src/{year}/day_{day}/input.txt"
            run(modulo, input_path)
    else:
        print('Something went wrong...')

    sys.exit()
