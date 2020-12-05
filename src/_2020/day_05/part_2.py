from .helper import get_seat_ids


def run(input_lines):
    """
    646
    """
    seat_id_list = get_seat_ids(input_lines)

    for seat in range(min(seat_id_list), max(seat_id_list)):
        if seat not in seat_id_list:
            return seat
