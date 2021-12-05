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


def part_1() -> int:
    coordinates = parse_input()
    grid_x = max([coodinate[0] for i in coordinates for coodinate in i]) + 1
    grid_y = max([coodinate[1] for i in coordinates for coodinate in i]) + 1
    grid = np.zeros([grid_x, grid_y], dtype=int)
    for (x1, y1), (x2, y2) in coordinates:
        x = sorted([x1, x2])
        x[1] += 1
        y = sorted([y1, y2])
        y[1] += 1
        if x1 == x2 or y1 == y2:
            grid[slice(*y), slice(*x)] += 1

    return dangerous_areas(grid)


if __name__ == "__main__":
    print("Part 1:", part_1())
