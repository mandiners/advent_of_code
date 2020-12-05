def convert_bin_to_dec(data, one, zero):
    return int(data.replace(one, '1').replace(zero, '0'), 2)


def get_seat_ids(lines):
    """
    Line example: 'FBFBBFFRLR'.
    Row is the first 7 characters from line: 'FBFBBFF' => 0101100 => 44.
    Column is the last 3 characters from line: 'RLR' => 101 => 5.
    Seat id is 8 * row + column = > 8 * 44 + 5 = 357
    """
    seat_ids = []

    for line in lines:
        row = convert_bin_to_dec(data=line[0:7], one='B', zero='F')
        column = convert_bin_to_dec(data=line[7::], one='R', zero='L')

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

    for seat in range(min(seat_id_list), max(seat_id_list)):
        if seat not in seat_id_list:
            return seat
