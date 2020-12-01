from collections import defaultdict


def overlap_checker(input_data):
    squares = {}
    results = defaultdict(int)
    for data in input_data:
        data = data.split(' ')
        x, y = [int(i) for i in data[2][:-1:].split(',')]
        a, b = [int(i) for i in data[3].split('x')]
        pk = int(data[0][1::])
        squares[pk] = {
            'x_range': (x, x + a),
            'y_range': (y, y + b)
        }

    for square in squares.values():
        left, right = square['x_range']
        up, down = square['y_range']
        for x in range(left + 1, right + 1):
            for y in range(up + 1, down + 1):
                results[(x, y)] += 1

    results = len([i for i in results.values() if i > 1])

    return results


def overlap_checker_2(input_data):
    squares = {}
    results = defaultdict(int)
    for data in input_data:
        data = data.split(' ')
        x, y = [int(i) for i in data[2][:-1:].split(',')]
        a, b = [int(i) for i in data[3].split('x')]
        pk = int(data[0][1::])
        squares[pk] = {
            'x_range': (x, x + a),
            'y_range': (y, y + b),
            'points': []
        }

    for square in squares.values():
        left, right = square['x_range']
        up, down = square['y_range']
        for x in range(left + 1, right + 1):
            for y in range(up + 1, down + 1):
                square['points'].append((x, y))
                results[(x, y)] += 1

    results = set([k for k, v in results.items() if v < 2])

    for pk, square in squares.items():
        checker = []
        for point in square['points']:
            if point in results:
                checker.append(point)
            else:
                break

            if len(checker) == len(square['points']):
                return pk

