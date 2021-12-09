from pathlib import Path
import pprint


class Heightmap:
    def __init__(self):
        self.heightmap = self.parse_input()

    def __repr__(self):
        return pprint.pformat(self.heightmap, width=302).replace(", ", "")

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

    @property
    def risk_level(self):
        return sum([i + 1 for i in self.low_points])


def part_1():
    heightmap = Heightmap()
    heightmap.find_low_points()
    return heightmap.risk_level


if __name__ == "__main__":
    print("Part 1:", part_1())
