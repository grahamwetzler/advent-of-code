from pathlib import Path

import numpy as np

np.set_printoptions(linewidth=100, formatter=dict(bool=lambda x: "#" if x else "."))


class Origami:
    def __init__(self, puzzle_input) -> None:
        self.coordinates, self.instructions = self._parse(puzzle_input)
        self._setup_grid()

    def _parse(self, puzzle_input) -> tuple[list]:
        c, i = puzzle_input.split("\n\n")
        return (
            [
                [int(x), int(y)]
                for x, y in [
                    coordinate.split(",") for coordinate in c.split("\n") if coordinate
                ]
            ],
            [instruction.split(" ")[2] for instruction in i.split("\n") if instruction],
        )

    def fold(self, instruction) -> None:
        axis, n = instruction.split("=")
        n = int(n)
        y_shape, x_shape = self.grid.shape
        if axis == "y":
            lower = np.flipud(self.grid[n + 1 :])
            upper = self.grid[:n]
            self.grid = upper + lower
        else:
            left = self.grid[:, :n]
            right = np.fliplr(self.grid[:, n + 1 :])
            self.grid = left + right

    def _setup_grid(self) -> None:
        grid_x_dimension = max([c[0] for c in self.coordinates]) + 1
        grid_y_dimension = max([c[1] for c in self.coordinates]) + 1
        self.grid = np.zeros((grid_y_dimension, grid_x_dimension), dtype=bool)
        for x, y in self.coordinates:
            self.grid[y][x] = True


def part_1(puzzle_input):
    origami = Origami(puzzle_input)
    origami.fold(origami.instructions[0])
    return origami.grid.sum()


def part_2(puzzle_input):
    origami = Origami(puzzle_input)
    for instruction in origami.instructions:
        origami.fold(instruction)
    return origami.grid


if __name__ == "__main__":
    puzzle_input = Path("2021/13/input.txt").read_text()
    print("Part 1:", part_1(puzzle_input))
    print("Part 2:", part_2(puzzle_input), sep="\n")
