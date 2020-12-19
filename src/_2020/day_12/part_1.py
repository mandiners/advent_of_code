from . import FORWARD, \
    LEFT, RIGHT, \
    EAST, \
    DIRECTIONS, \
    ORDER_OF_DIRECTIONS
from .helper import compass


def turn_the_ship(value, direction, degree):
    quarter = int(degree / 90)
    index = quarter % 4

    if direction == RIGHT:
        temp_direction = compass(ORDER_OF_DIRECTIONS, value)
    else:
        temp_direction = compass([i for i in reversed(ORDER_OF_DIRECTIONS)], value)

    return temp_direction[index]


def run(input_lines):
    """
    420
    """
    actions = [i for i in input_lines]
    ship = {'x': 0,
            'y': 0,
            'facing': EAST}

    for action in actions:
        direction = action[0]
        value = int(action[1::])

        if direction in [RIGHT, LEFT]:
            ship['facing'] = turn_the_ship(ship['facing'], direction, value)
        else:
            temp = DIRECTIONS[direction] if direction != FORWARD else DIRECTIONS[ship['facing']]
            axis, operator = temp['axis'], temp['operator']
            ship[axis] += int(f"{operator}{value}")

    return abs(ship['x']) + abs(ship['y'])
