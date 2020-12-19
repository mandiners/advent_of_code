from . import FORWARD, \
    LEFT, RIGHT, \
    NORTH, EAST, SOUTH, WEST, \
    POSITIVE, \
    DIRECTIONS, \
    ORDER_OF_DIRECTIONS
from .helper import compass


def calculate_new_waypoint(x, y, waypoint, reverse=False):
    waypoint_x = 'x' if not reverse else 'y'
    waypoint_y = 'y' if not reverse else 'x'

    if DIRECTIONS[x]['operator'] == POSITIVE:
        temp_x = abs(waypoint[waypoint_x])
    else:
        temp_x = abs(waypoint[waypoint_x]) * -1

    if DIRECTIONS[y]['operator'] == POSITIVE:
        temp_y = abs(waypoint[waypoint_y])
    else:
        temp_y = abs(waypoint[waypoint_y]) * -1

    return temp_x, temp_y


def turn_the_waypoint(direction, degree, waypoint):
    quarter = int(degree / 90)
    index = quarter % 4
    temp_waypoint_x = WEST if waypoint['x'] < 0 else EAST
    temp_waypoint_y = SOUTH if waypoint['y'] < 0 else NORTH

    if direction == RIGHT:
        temp_directions_for_x = compass(ORDER_OF_DIRECTIONS, temp_waypoint_x)
        temp_directions_for_y = compass(ORDER_OF_DIRECTIONS, temp_waypoint_y)
    else:
        temp_directions_for_x = compass([i for i in reversed(ORDER_OF_DIRECTIONS)], temp_waypoint_x)
        temp_directions_for_y = compass([i for i in reversed(ORDER_OF_DIRECTIONS)], temp_waypoint_y)

    x = temp_directions_for_x[index]
    y = temp_directions_for_y[index]

    if index % 2 == 0:
        return calculate_new_waypoint(x, y, waypoint)
    else:
        return calculate_new_waypoint(y, x, waypoint, reverse=True)


def run(input_lines):
    """
    42073
    """
    actions = [i for i in input_lines]
    ship = {'x': 0,
            'y': 0,
            'facing': EAST}

    waypoint = {'x': 10, 'y': 1}

    for action in actions:
        direction = action[0]
        value = int(action[1::])

        if direction in [RIGHT, LEFT]:
            waypoint['x'], waypoint['y'] = turn_the_waypoint(direction, value, waypoint)
        elif direction == FORWARD:
            ship['x'] += waypoint['x'] * value
            ship['y'] += waypoint['y'] * value
        else:
            temp = DIRECTIONS[direction]
            axis, operator = temp['axis'], temp['operator']
            waypoint[axis] += int(f"{operator}{value}")

    return abs(ship['x']) + abs(ship['y'])
