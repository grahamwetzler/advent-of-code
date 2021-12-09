from math import prod
from pathlib import Path

import numpy as np
import scipy.ndimage


class Heightmap:
    def __init__(self):
        self.heightmap = self.parse_input()

    def parse_input(self):
        text = Path("2021/09/input.txt").read_text()
        heightmap = []
        for row in text.split("\n"):
            rows = []
            if row:
                for value in row:
                    rows.append(int(value))
                heightmap.append(rows)
        return heightmap

    def find_low_points(self):
        self.low_points = []
        for row_idx, row in enumerate(self.heightmap):
            for col_idx, value in enumerate(row):
                comparison_values = []

                if col_idx - 1 >= 0:
                    comparison_values.append(self.heightmap[row_idx][col_idx - 1])

                try:
                    comparison_values.append(self.heightmap[row_idx][col_idx + 1])
                except IndexError:
                    pass

                if row_idx - 1 >= 0:
                    comparison_values.append(self.heightmap[row_idx - 1][col_idx])

                try:
                    comparison_values.append(self.heightmap[row_idx + 1][col_idx])
                except IndexError:
                    pass

                if value < min(comparison_values):
                    self.low_points.append(value)

        return self

    def n_largest_basins(self, n):
        array = np.array(self.heightmap)
        basin_mask = array < 9
        labels = scipy.ndimage.label(basin_mask)
        labels, heightmap_counts = labels
        basins = []
        for group in range(1, heightmap_counts + 1):
            basins.append((labels == group).sum())
        basins.sort()

        return basins[-n:]

    @property
    def risk_level(self):
        return sum([i + 1 for i in self.low_points])


def part_1():
    heightmap = Heightmap()
    heightmap.find_low_points()
    return heightmap.risk_level


def part_2():
    heightmap = Heightmap()
    heightmap.find_low_points()
    basins = heightmap.n_largest_basins(3)
    return prod(basins)


if __name__ == "__main__":
    print("Part 1:", part_1())
    print("Part 2:", part_2())
