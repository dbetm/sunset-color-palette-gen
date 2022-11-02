from typing import List


def gen_columns(num_colors_per_row: int) -> List[str]:
    channels_map = ("red", "blue", "green")
    number_channels = 3

    columns = list()

    for i in range(num_colors_per_row * number_channels):
        c_name = f"{channels_map[i % number_channels]}{i // 3}"
        columns.append(c_name)

    return columns