FLOOR = '.'
EMPTY = 'L'
OCCUPIED = '#'
DIRECTIONS = [
    (-1, 0),
    (-1, -1),
    (0, -1),
    (1, -1),
    (0, 1),
    (1, 1),
    (1, 0),
    (-1, 1)
]


def is_valid_seat(x, y, x_threshold, y_threshold, seats):
    if x < 0 or y < 0 or x >= x_threshold or y >= y_threshold:
        return False
    return seats[x][y]
