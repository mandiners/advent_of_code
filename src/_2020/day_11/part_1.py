from .helper import FLOOR, EMPTY, OCCUPIED, DIRECTIONS, is_valid_seat


def calculate_empty(row, column, seats):
    x_threshold = len(seats)
    y_threshold = len(seats[0])

    for direction in DIRECTIONS:
        x, y = row, column
        x += direction[0]
        y += direction[1]

        current_seat = is_valid_seat(x, y, x_threshold, y_threshold, seats)
        if not current_seat:
            break

        if current_seat == OCCUPIED:
            return EMPTY

    return OCCUPIED


def calculate_occupied(row, column, seats):
    occupied_seat_in_sight = 0

    x_threshold = len(seats)
    y_threshold = len(seats[row])

    for direction in DIRECTIONS:
        x, y = row, column
        x += direction[0]
        y += direction[1]

        current_seat = is_valid_seat(x, y, x_threshold, y_threshold, seats)
        if not current_seat:
            break

        if current_seat == OCCUPIED:
            occupied_seat_in_sight += 1

        if occupied_seat_in_sight >= 4:
            return EMPTY

    return OCCUPIED


def check_point(row, column, seats):
    point = seats[row][column]

    if point == EMPTY:
        return calculate_empty(row, column, seats)
    elif point == OCCUPIED:
        return calculate_occupied(row, column, seats)
    else:
        return FLOOR


def run(input_lines):
    """
    2354
    """
    seats = [i for i in input_lines]

    new_seats = None
    is_changed = True

    while is_changed:
        seats = new_seats if new_seats else seats
        temp_seats = []
        for row, seat in enumerate(seats):
            temp_seats.append([])
            for column, c_seat in enumerate(seat):
                new_seat = check_point(row, column, seats)
                temp_seats[-1].append(new_seat)

        if seats == temp_seats:
            is_changed = False
        else:
            new_seats = temp_seats

    result = len([val for line in new_seats for val in line if val == OCCUPIED])

    return result
