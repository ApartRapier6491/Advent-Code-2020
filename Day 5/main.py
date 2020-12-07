from typing import List

FILENAME = "input.txt"

def get_input() -> List[str]:
    """ Read the file and generate a list of seat strings

    Returns:
        [List[str]]: A list of seat strings
    """
    seats = list()

    with open(FILENAME) as f:
        for line in f.readlines():
            seats.append(line.strip())

    return seats

def get_seat_ID(seat_string: str) -> int:
    """Take in seat string and calculate its ID.

    Args:
        seat_string (str): self-explantory

    Returns:
        int: seat ID
    """
    row_string = seat_string[:-3]
    col_string = seat_string[-3:]

    row_binary = row_string.replace('F', '0').replace('B', '1')
    col_binary = col_string.replace('L', '0').replace('R', '1')

    row_num = int(row_binary, 2)
    col_num = int(col_binary, 2)

    return 8*row_num + col_num

def part_1():
    seat_strings = get_input()
    max_ID = 0

    for seat_string in seat_strings:
        max_ID = max(max_ID, get_seat_ID(seat_string))

    print(f"The highest seat ID on a boarding pass is {max_ID}")

def part_2():
    seat_strings = get_input()
    set_seat_ID = set()

    for seat_string in seat_strings:
        set_seat_ID.add(get_seat_ID(seat_string))

    for i in range(min(set_seat_ID)+1, max(set_seat_ID)):
        if i not in set_seat_ID:
            print(f"The ID if your seat is {i}")
            break

if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
