import datetime as dt
from utils.parser import input_parser
from twenty_eighteen_1.handler import calculator


if __name__ == '__main__':
    data = [i.rstrip() for i in input_parser('twenty_eighteen_1/input.txt')]
    start_time = dt.datetime.now()
    result = calculator(data)
    print(f"Run time: {dt.datetime.now() - start_time}")
    print(result)
