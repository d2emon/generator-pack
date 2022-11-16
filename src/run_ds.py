import random


def get_middle(value1, value2):
    delta = 1 * 0.01
    middle = (value1 + value2) / 2
    middle += middle * random.uniform(-delta, delta)
    if middle < 0:
        middle = 0
    if middle > 100:
        middle = 100
    return middle


def diamond_square_row(item1, item2):
    middle = get_middle(item1, item2)
    return [
        item1,
        middle,
        item2,
    ]


def diamond_square_subblock(block):
    row0, row1 = block

    middle0 = get_middle(row0[0], row1[0])
    middle1 = get_middle(row0[1], row1[1])
    return [
        diamond_square_row(row0[0], row0[1]),
        diamond_square_row(middle0, middle1),
        diamond_square_row(row1[0], row1[1]),
    ]


def diamond_square(start):
    width = len(start) - 1
    length = len(start[0]) - 1
    result = [
        [
            0
            for _ in range(length * 2 + 1)
        ]
        for _ in range(width * 2 + 1)
    ]

    for row_id in range(width):
        for col_id in range(length):
            subblock = diamond_square_subblock([
                [
                    start[i][j]
                    for j in range(col_id, col_id + 2)
                ]
                for i in range(row_id, row_id + 2)
            ])

            new_row_id = row_id * 2
            new_col_id = col_id * 2
            for subrow_id, subrow in enumerate(subblock):
                for subcol_id, item in enumerate(subrow):
                    result[new_row_id + subrow_id][new_col_id + subcol_id] = item

    return result


def get_char(value):
    DEEP = '\033[94m'
    WATER = '\033[36m'
    MOUNTAINS = '\033[37m'
    HILLS = '\033[33m'
    FOREST = '\033[32m'
    GRASSLANDS = '\033[92m'
    COASTLINE = '\033[93m'

    if value > 90:
        color = MOUNTAINS
    elif value > 80:
        color = HILLS
    elif value > 70:
        color = FOREST
    elif value > 60:
        color = GRASSLANDS
    elif value > 50:
        color = COASTLINE
    elif value > 25:
        color = WATER
    else:
        color = DEEP

    value = int(value)
    if value < 50:
        char_id = int(122 - 25 * (value / 50))
    else:
        char_id = int(65 + 25 * ((value - 50) / 50))

    return color + chr(char_id)

if __name__ == "__main__":
    start_size = 2
    block = [
        [
            random.uniform(0, 100)
            for _ in range(start_size)
        ]
        for _ in range(start_size)
    ]

    WARNING = '\033[91m'
    while len(block) < 100:
        block = diamond_square(block)
        print(WARNING + "=" * 80)
        for row in block:
            print("".join(get_char(chr_id) for chr_id in row))
