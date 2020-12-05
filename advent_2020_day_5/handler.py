def get_seat_ids(lines):
    seat_ids = []

    for line in lines:
        row = line[0:7]
        column = line[7::]

        row = int(''.join('0' if r == 'F' else '1' for r in row), 2)
        column = int(''.join('0' if c == 'L' else '1' for c in column), 2)
        seat_id = (8 * row) + column

        seat_ids.append(seat_id)

    return seat_ids


def get_max_seat_id(input_lines):
    """
    974
    """
    return max(get_seat_ids(input_lines))


def seat_locator(input_lines):
    """
    646
    """
    seat_id_list = get_seat_ids(input_lines)

    for seat in range(min(seat_id_list) - 1, max(seat_id_list) + 1):
        if seat not in seat_id_list:
            return seat
