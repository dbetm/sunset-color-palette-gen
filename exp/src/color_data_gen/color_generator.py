import csv
import os
from math import ceil

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
from tqdm import tqdm


class ColorGenerator:
    def __init__(self, path: str, csv_path: str):
        self.path = path
        self.csv_path = csv_path
        self.headers = [
            'file_name',
            'color_1',
            'color_2',
            'color_3',
            'color_4',
            'color_5', 
            'color_6',
        ]

    def _get_kmeans_centers(self, img, nclusters: int):
        return KMeans(n_clusters=nclusters).fit(img).cluster_centers_

    def _get_image(self, path: str):
        with open(path, "rb") as f:
            return np.array(Image.open(f))

    def _preprocess_image(self, image):
        return image.reshape((-1, 3)).astype("float32") / 255

    def _plot_palette(self, centers: np.ndarray) -> None:
        plt.figure(figsize=(14, 6))
        plt.imshow(centers[
            np.concatenate(
                [[i] * 100 for i in range(len(centers))]).reshape((-1, 10)).T
        ])
        plt.grid()
        plt.axis('off')
        plt.show()

    def generate_colors(self, nclusters: int, show_palette: bool) -> None:
        dataset = os.listdir(self.path)
        file = open(self.csv_path, 'w', encoding='UTF8', newline='')
        writer = csv.writer(file)
        writer.writerow(self.headers)

        for image in tqdm(dataset):
            entry = [image]
            img = self._get_image(os.path.join(self.path, image))
            rgb_pixels = self._preprocess_image(img)
            centers = self._get_kmeans_centers(rgb_pixels, nclusters)
            entry.extend(
                [
                    ';'.join(map(lambda a: str(ceil(a * 255)), i))
                    for i in centers
                ]
            )
            if show_palette:
                self._plot_palette(centers)

            writer.writerow(entry)


gen = ColorGenerator(path='dataset', csv_path='data_test.csv')
gen.generate_colors(6, False)
