def overlap_checker(input_data):
    squares = {}
    for data in input_data:
        data = data.split(' ')
        x, y = data[2].split(',')
        a, b = data[3].split('x')
        pk = int(data[0][1::])
        squares[pk] = {
            'x': int(x),
            'y': int(y[:-1:]),
            'a': int(a),
            'b': int(b)
        }

    # print(max(i['x'] for i in squares.values()))
    # print(max(i['y'] for i in squares.values()))

    return squares
