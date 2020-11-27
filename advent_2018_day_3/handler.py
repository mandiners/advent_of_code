import asyncio

loop = asyncio.get_event_loop()


async def checker(point, kockak):
    match = 0
    for square in kockak.values():
        if match > 1:
            return point
        else:
            left, right = square['x_range']
            up, down = square['y_range']
            if point[0] in range(left, right) and point[1] in range(up, down):
                match += 1


async def run(foo, bar):
    print(foo)
    await asyncio.gather(*[checker(i, bar) for i in foo])


def overlap_checker(input_data):
    squares = {}
    results = []
    for data in input_data:
        data = data.split(' ')
        x, y = data[2].split(',')
        a, b = data[3].split('x')
        pk = int(data[0][1::])
        squares[pk] = {
            'x_range': (int(x) + 1, int(x) + int(a)),
            'y_range': (int(y[:-1:]) + 1, int(y[:-1:]) + int(b))
        }

    x_coordinates = range(1, max(int(i['x_range'][1] + 1) for i in squares.values()))
    y_coordinates = range(1, max(int(i['y_range'][1] + 1) for i in squares.values()))
    foo = [(x, y) for x in x_coordinates for y in y_coordinates]
    try:
        loop.run_until_complete(run(foo, squares))
    finally:
        loop.close()
    # for x in x_coordinates:
    #     for y in y_coordinates:
    #         match = 0
    #         for square in squares.values():
    #             if match > 3:
    #                 results.append([x, y])
    #                 break
    #             else:
    #                 left, right = square['x_range']
    #                 up, down = square['y_range']
    #                 if x in range(left, right) and y in range(up, down):
    #                     match += 1

    return foo
