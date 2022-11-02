
"""Program to read from a csv file and print the colors in the file."""
import csv
import random
from math import sqrt
from typing import List

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from tqdm import tqdm

from utils import gen_columns


# given an array of colors, where the ith position its a triple with
# the r, g, b format of the ith color, show them in a row in a graphic way

def show_colors(colors):
    #create a figure with the same size as the number of colors
    fig = plt.figure(figsize=(len(colors), 1))
    #add an axis
    ax = fig.add_subplot(111)
    #set the axis limits
    ax.set_xlim(0, len(colors))
    ax.set_ylim(0, 1)
    #set the axis to be invisible
    ax.set_axis_off()
    #add the colors to the axis
    ax.imshow([colors])
    #show the figure
    plt.show()


# given a two dimensional array
# where the first dimension is the number of colors
# and the second dimension is an array with the ith position its a triple with the r, g, b format of a color
# show the two dimensional array in a graphic way

def show_colors_2d(colors):
    #create a figure with the same size as the number of colors
    fig = plt.figure(figsize=(len(colors[0]), len(colors)))
    #add an axis
    ax = fig.add_subplot(111)
    #set the axis limits
    ax.set_xlim(0, len(colors[0]))
    ax.set_ylim(0, len(colors))
    #set the axis to be invisible
    #ax.set_axis_off()
    #add the colors to the axis
    ax.imshow(colors)

    #show the figure, showing the x values so that it fits the figure

    plt.show()


# FUNCTIONS FOR KMEANS ALGORITHM


class Point:
    def __init__(self, coordinates):
        self.coordinates = coordinates


class Cluster:

    def __init__(self, center, points):
        self.center = center
        self.points = points

class KMeans:
    def __init__(self, n_clusters, min_diff = 1):
        self.n_clusters = n_clusters
        self.min_diff = min_diff

    def calculate_center(self, points):
        n_dim = len(points[0].coordinates)
        vals = [0.0 for i in range(n_dim)]
        for p in points:
            for i in range(n_dim):
                vals[i] += p.coordinates[i]
        coords = [(v / len(points)) for v in vals]
        return Point(coords)

    def assign_points(self, clusters, points):
        plists = [[] for i in range(self.n_clusters)]

        for p in points:
            smallest_distance = float('inf')

            for i in range(self.n_clusters):
                distance = euclidean(p, clusters[i].center)
                if distance < smallest_distance:
                    smallest_distance = distance
                    idx = i

            plists[idx].append(p)

        return plists

    def fit(self, points):
        clusters = [
            Cluster(center=p, points=[p]) for p in random.sample(points, self.n_clusters)
        ]

        while True:
            plists = self.assign_points(clusters, points)
            diff = 0

            for i in range(self.n_clusters):
                if not plists[i]:
                    continue
                old = clusters[i]
                center = self.calculate_center(plists[i])
                new = Cluster(center, plists[i])
                clusters[i] = new
                diff = max(diff, euclidean(old.center, new.center))

            if diff < self.min_diff:
                break

        return clusters


def euclidean(p, q):
    n_dim = len(p.coordinates)
    return sqrt(sum([
        (p.coordinates[i] - q.coordinates[i]) ** 2 for i in range(n_dim)
    ]))


def rgb_to_hex(rgb):
    return '#%s' % ''.join(('%02x' % p for p in rgb))


def get_points_pro(row):
    points = []

    for color in row:
        points.append(Point(color))
        #print(color)

    return points


def get_colors_pro(n_colors=3, rowx = []):
    points = get_points_pro(rowx)
    clusters = KMeans(n_clusters=n_colors).fit(points)
    clusters.sort(key=lambda c: len(c.points), reverse = True)
    rgbs = [map(int, c.center.coordinates) for c in clusters]
    return list(map(rgb_to_hex, rgbs))


#given an array of colors, where the ith position its a triple with the r, g, b format of the ith color, show them in a row in a graphic way
def show_colors(colors, title):
    #create a figure with the same size as the number of colors
    fig = plt.figure(figsize=(len(colors), 1))
    #add an axis
    ax = fig.add_subplot(111)
    #set the axis limits
    ax.set_xlim(0, len(colors))
    ax.set_ylim(0, 1)
    #set the axis to be invisible
    ax.set_axis_off()
    #add the colors to the axis
    ax.imshow([colors])
    #add the title
    plt.title(title)
    #show the figure
    plt.show()


#given a two dimensional array
#where the first dimension is the number of colors
#and the second dimension is an array with the ith position its a triple with the r, g, b format of a color
#show the two dimensional array in a graphic way
def show_colors_2d(colors, title):
    #create a figure with the same size as the number of colors
    fig = plt.figure(figsize=(len(colors[0]), len(colors)))
    #add an axis
    ax = fig.add_subplot(111)
    #set the axis limits
    ax.set_xlim(0, len(colors[0]))
    ax.set_ylim(0, len(colors))
    #set the axis to be invisible
    #ax.set_axis_off()
    #add the colors to the axis
    ax.imshow(colors)
    #add the title
    plt.title(title)
    #show the figure, showing the x values so that it fits the figure
    plt.show()


def get_k_colors_from_all_dataset(k: int, data: List[tuple]) -> List[tuple]:
    #group ALL the colors using kmeans
    kcolors = get_colors_pro(n_colors=k, rowx=data)

    ", ".join(kcolors)

    # print(kcolors) #prints ALL the k colors in dataset in hex format

    #convert ALL kcolors in dataset from hex to rgb
    colors_rgb = []
    for color in kcolors:
        color = color.lstrip('#')
        lv = len(color)
        colors_rgb.append(tuple(int(color[i:i + lv // 3], 16) for i in range(0, lv, lv // 3)))

    # print(colors_rgb)  #prints ALL the k colors in dataset in rgb format
    # show_colors(colors_rgb, "K colores del dataset")   #Muestra los colores de la n-esima fila agrupados en kcolores

    return colors_rgb


def gen_color_group_hash(color_group: list) -> str:
    color_hash = ""

    for color in color_group:
        color_hash += "".join(map(str, color))

    return color_hash


def gen_sample_colors(all_colors: list, sample_frac: float = 0.8) -> list:
    sample = list()
    n = len(all_colors)
    s_size = int(n * sample_frac)

    assert s_size >= 5

    for _ in range(s_size):
        idx = random.randint(0, n-1)
        sample.append(all_colors[idx])


    return sample



# main function
if __name__ == '__main__':
    # given a two dimensional array
    # where every column is an array with the ith position its a triple with the r, g, b format of a color
    # group the array using kmeans
    # and return the groups

    # Agrupar en k colores
    K = 4
    RAW_DATASET_PATH = "exp/src/color_data_gen/data.csv"
    OUTPUT_DATASET_PATH = "exp/src/processed_color_data.csv"

    all_colors = []

    with open(RAW_DATASET_PATH) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')

        colors = []
        cont = 0

        for row in readCSV:
            if cont == 0:
                cont += 1
                # skip the header
                continue

            if(len(row) == 4):
                pass
                # print(row[0], row[1], row[2], row[3])

            elif(len(row) == 7):
                # print(row[0], row[1], row[2], row[3], row[4], row[5], row[6])

                columns = []

                #store the values of the colors in an array of triples
                for i in range(1, len(row)):
                    columns.append((int(row[i][0:row[i].find(';')]) , int(row[i][row[i].find(';')+1:row[i].rfind(';')]), int(row[i][row[i].rfind(';')+1:])))
                    all_colors.append((int(row[i][0:row[i].find(';')]) , int(row[i][row[i].find(';')+1:row[i].rfind(';')]), int(row[i][row[i].rfind(';')+1:])))

                #print(columns)          #[(73, 55, 84), (234, 227, 221), (4, 3, 4), (147, 86, 101), (213, 146, 140), (33, 34, 59)]
                #print(columns[0])       #(73, 55, 84)
                colors.append(columns)

                """
                show colors row by row in a graphic way
                show_colors(colors[cont], "Colores raw " + "fila " + str(cont) )   #Muestra los colores de la n-esima fila
                """

                """
                #group the colors using kmeans
                kcolors = get_colors_pro(n_colors=K, rowx = columns)
                ", ".join(kcolors)

                #print(kcolors) #prints the k colors in hex format

                #convert colors row by row from hex to rgb
                colors_rgb = []
                for color in kcolors:
                    color = color.lstrip('#')
                    lv = len(color)
                    colors_rgb.append(tuple(int(color[i:i + lv // 3], 16) for i in range(0, lv, lv // 3)))

                #print(colors_rgb) #prints the k colors in rgb format
                """

                """
                show_colors(colors_rgb, "K colores " + "fila " + str(cont) )   #Muestra los colores de la n-esima fila agrupados en kcolores
                """
                cont += 1

        # show_colors_2d(colors, "Colores raw")  #Muestra los colores de todas las filas en una sola imagen
        # where colors is a 2d array like:
        """
        [(35, 29, 28), (215, 194, 170), (152, 109, 92), (247, 244, 229), (90, 63, 56), (225, 144, 84)]
        [(32, 17, 11), (196, 137, 90), (233, 142, 36), (146, 84, 42), (77, 68, 61), (81, 40, 22)]
        """

        # Imprime todos los colores del dataset en RGB, en un solo arreglo de 1D
        # print("Todos los colores:")
        # print(all_colors)
    unique_representative_color_groups = list()
    color_hashes = set()

    for _ in tqdm(range(100)):
        sample_colors = gen_sample_colors(all_colors)
        row = get_k_colors_from_all_dataset(k=K, data=sample_colors)
        row.sort(reverse=True)
        color_group_hash = gen_color_group_hash(row)

        if color_group_hash not in color_hashes:
            color_hashes.add(color_group_hash)
            flatten_row = list(sum(row, ()))
            unique_representative_color_groups.append(flatten_row)

    columns = gen_columns(num_colors_per_row=K)

    df = pd.DataFrame(unique_representative_color_groups, columns=columns)

    df.to_csv(OUTPUT_DATASET_PATH, index=False, header=False)
