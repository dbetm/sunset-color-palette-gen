"""Generates a new dataset, with K colors from each image and sorted (clarity-dark).
"""
import pandas as pd

from utils import gen_columns

K = 4


def convert_color_to_tuple(color: str) -> tuple:
    return tuple(map(int, color.split(";")))


def create_color_group(k: int, row: dict) -> list:
    color_group = [
        convert_color_to_tuple(row[f"color_{i}"])
        for i in range(1, 7)
    ]
    color_group.sort(reverse=True)

    return list(sum(color_group[0:k], ()))


if __name__ == '__main__':
    new_data = list()
    data = pd.read_csv("data.csv")

    for idx, row in data.iterrows():
        color_group = create_color_group(K, row)

        new_data.append(color_group)

    cols = gen_columns(num_colors_per_row=4)
    new_df = pd.DataFrame(data=new_data, columns=cols)

    new_df.to_csv("curated_dataset.csv", header=False, index=False)