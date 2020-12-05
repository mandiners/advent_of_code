import argparse
import datetime as dt
import src
import sys
from utils.helper import input_loader, format_data, get_args


def run(callback, path):
    # Start Timer
    start_time = dt.datetime.now()

    # Parsing
    raw_data = input_loader(path)
    data = format_data(raw_data)

    # Run
    result = callback(data)

    # End of Task
    print(f"Run time: {dt.datetime.now() - start_time}")
    print(f"Result: {result}")


if __name__ == '__main__':
    args = get_args()
    year, day, part = args.year, args.day, args.part

    year_module = getattr(src, f"_{year}", None)
    if not year_module:
        print(f'Cannot import src.{year}')
        sys.exit(1)

    day_module = getattr(year_module, f"day_{day}", None)
    if not day_module:
        print(f'Cannot import src.{year}.day_{day}')
        sys.exit(1)

    _module = getattr(day_module, f"part_{part}", None)
    if not _module:
        print(f'Cannot import src.{year}.day_{day}.part_{part}')
        sys.exit(1)

    if hasattr(_module, 'run'):
        input_path = f"src/_{year}/day_{day}/input.txt"
        run(_module.run, input_path)
    else:
        print('Something went wrong...')
