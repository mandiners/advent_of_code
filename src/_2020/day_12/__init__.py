RIGHT = 'R'
LEFT = 'L'

FORWARD = 'F'

EAST = 'E'
WEST = 'W'
NORTH = 'N'
SOUTH = 'S'

POSITIVE = '+'

ORDER_OF_DIRECTIONS = (NORTH, EAST, SOUTH, WEST)

DIRECTIONS = {
    NORTH: {'axis': 'y', 'operator': '+'},
    EAST: {'axis': 'x', 'operator': '+'},
    SOUTH: {'axis': 'y', 'operator': '-'},
    WEST: {'axis': 'x', 'operator': '-'},
}
