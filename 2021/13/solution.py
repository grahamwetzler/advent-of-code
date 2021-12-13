from pathlib import Path

import numpy as np

np.set_printoptions(linewidth=100, formatter={"bool": lambda x: "#" if x else "."})


class Origami:
    def __init__(self, puzzle_input: str) -> None:
        self.coordinates, self.instructions = self._parse(puzzle_input)
        self._initialize_grid()

    def fold(self, instruction: str) -> None:
        axis, n = instruction.split("=")
        n = int(n)
        if axis == "y":
            lower = np.flipud(self.grid[n + 1 :, ...])
            upper = self.grid[:n, ...]
            self.grid = upper + lower
        else:
            left = self.grid[..., :n]
            right = np.fliplr(self.grid[..., n + 1 :])
            self.grid = left + right

    def _parse(self, puzzle_input: str) -> tuple[list]:
        coordinates, instructions = puzzle_input.split("\n\n")
        return (
            [
                [int(x), int(y)]
                for x, y in [
                    coordinate.split(",")
                    for coordinate in coordinates.split("\n")
                    if coordinate
                ]
            ],
            [
                instruction.split(" ")[2]
                for instruction in instructions.split("\n")
                if instruction
            ],
        )

    def _initialize_grid(self) -> None:
        x_dim = max([x for x, _ in self.coordinates]) + 1
        y_dim = max([y for _, y in self.coordinates]) + 1
        self.grid = np.zeros((y_dim, x_dim), dtype=bool)
        for x, y in self.coordinates:
            self.grid[y][x] = True


def part_1(puzzle_input: str) -> int:
    origami = Origami(puzzle_input)
    origami.fold(origami.instructions[0])
    return origami.grid.sum()


def part_2(puzzle_input: str) -> np.ndarray:
    origami = Origami(puzzle_input)
    for instruction in origami.instructions:
        origami.fold(instruction)
    return origami.grid


if __name__ == "__main__":
    puzzle_input = Path("2021/13/input.txt").read_text()
    print("Part 1:", part_1(puzzle_input))
    print("Part 2:", part_2(puzzle_input), sep="\n")
