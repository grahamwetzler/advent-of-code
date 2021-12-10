from pathlib import Path

import numpy as np


def parse_input() -> list:
    puzzle_input = Path("2021/05/input.txt").read_text()
    segments = puzzle_input.split("\n")
    pairs = [p.split(" -> ") for p in segments if p]
    coordinates = [(eval(p1), eval(p2)) for (p1, p2) in pairs]
    return coordinates


def dangerous_areas(array: np.array, threshold: int = 2) -> int:
    return (array >= threshold).sum()


def part_1_and_2():
    coordinates = parse_input()
    grid_dims = max([coodinate[0] for i in coordinates for coodinate in i]) + 1
    grid = np.zeros((grid_dims, grid_dims), dtype=int)
    for (x1, y1), (x2, y2) in coordinates:
        if (x1 == x2) or (y1 == y2):
            if (x1 < x2) or (y1 < y2):
                grid[x1 : x2 + 1, y1 : y2 + 1] += 1
            elif (x1 > x2) or (y1 > y2):
                grid[x2 : x1 + 1, y2 : y1 + 1] += 1

    print("Part 1:", dangerous_areas(grid))

    for (x1, y1), (x2, y2) in coordinates:
        if (x1 != x2) and (y1 != y2):
            x_step = -1 if x1 > x2 else 1
            y_step = -1 if y1 > y2 else 1

            for x, y in zip(
                range(x1, x2 + x_step, x_step), range(y1, y2 + y_step, y_step)
            ):
                grid[x, y] += 1

    print("Part 2:", dangerous_areas(grid))


if __name__ == "__main__":
    part_1_and_2()
