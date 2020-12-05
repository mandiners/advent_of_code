from collections import defaultdict


def run(input_data):
    """
    105231
    """
    squares = {}
    results = defaultdict(int)
    for data in input_data:
        data = data.split(' ')
        x, y = [int(i) + 1 for i in data[2][:-1:].split(',')]
        a, b = [int(i) for i in data[3].split('x')]
        pk = int(data[0][1::])
        squares[pk] = {
            'x_range': (x, x + a),
            'y_range': (y, y + b)
        }

    for square in squares.values():
        left, right = square['x_range']
        up, down = square['y_range']
        for x in range(left, right):
            for y in range(up, down):
                results[(x, y)] += 1

    results = len([i for i in results.values() if i > 1])

    return results
