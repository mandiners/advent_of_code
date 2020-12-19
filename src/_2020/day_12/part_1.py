from . import FORWARD,\
    LEFT, RIGHT,\
    NORTH, EAST, SOUTH, WEST,\
    ORDER_OF_DIRECTIONS

DIRECTIONS = {
    NORTH: {'axis': 'y', 'operator': '+'},
    EAST: {'axis': 'x', 'operator': '+'},
    SOUTH: {'axis': 'y', 'operator': '-'},
    WEST: {'axis': 'x', 'operator': '-'},
}


def compass(direction, value):
    start = direction.index(value)

    return [*[direction[start]],
            *[i for i in direction[start::] if i != direction[start]],
            *[j for j in direction[:start:] if j != direction[start]]]


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
