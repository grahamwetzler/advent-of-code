from dataclasses import dataclass
from pathlib import Path


@dataclass
class Octopus:
    energy_level: int
    flashed: bool = False
    flashes: int = 0

    def __str__(self) -> str:
        if self.flashed:
            return f"\033[93;1m{self.energy_level}\033[0m"
        else:
            return f"{self.energy_level}"

    def step(self) -> bool:
        """Returns True if flashed, otherwise False."""
        if not self.flashed:
            self.energy_level += 1
        else:
            return False

        if self.energy_level > 9:
            self.flashed = True
            self.flashes += 1
            self.energy_level = 0
            return True

        return False


class Grid:
    def __init__(self, grid: str) -> None:
        self.grid = self._parse_grid(grid)

    def __repr__(self) -> str:
        return "\n".join(["".join([str(o) for o in row]) for row in self.grid])

    def _parse_grid(self, grid: str) -> list[list[int]]:
        return [[Octopus(int(i)) for i in row] for row in grid.split("\n") if row]

    def _is_valid(self, row_idx: int, col_idx: int) -> bool:
        """Checks if row and column are valid octopi."""
        if 0 <= row_idx <= len(self.grid) - 1 and 0 <= col_idx <= len(self.grid[0]) - 1:
            return True
        return False

    def _step_adjacent(self, row_idx: int, col_idx: int) -> None:
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                adjacent_y, adjacent_x = row_idx + y, col_idx + x
                if not (x == y == 0) and self._is_valid(adjacent_y, adjacent_x):
                    octopus = self.grid[adjacent_y][adjacent_x]
                    if octopus.step():
                        self._step_adjacent(adjacent_y, adjacent_x)

    def _reset_flashes(self) -> None:
        for row in self.grid:
            for octopus in row:
                octopus.flashed = False

    def _step(self) -> None:
        for row_idx, row in enumerate(self.grid):
            for col_idx, octopus in enumerate(row):
                if octopus.step():
                    self._step_adjacent(row_idx, col_idx)

    def step_n_times(self, times: int) -> None:
        for _ in range(times):
            self._step()
            self._reset_flashes()

    @property
    def steps_until_simultaneous_flash(self) -> int:
        step = 0
        while True:
            step += 1
            self._step()

            if all([octopus.flashed for row in self.grid for octopus in row]):
                break

            self._reset_flashes()

        return step

    @property
    def flashes(self) -> int:
        return sum([octopus.flashes for row in self.grid for octopus in row])


def part_1(puzzle_input: str) -> int:
    grid = Grid(puzzle_input)
    grid.step_n_times(times=100)
    return grid.flashes


def part_2(puzzle_input: str) -> int:
    grid = Grid(puzzle_input)
    return grid.steps_until_simultaneous_flash


if __name__ == "__main__":
    puzzle_input = Path("2021/11/input.txt").read_text()
    print("Part 1:", part_1(puzzle_input))
    print("Part 2:", part_2(puzzle_input))
