from pathlib import Path
from queue import PriorityQueue

import numpy as np


class Cavern:
    def __init__(self, puzzle_input: str) -> None:
        self.map = self._parse_input(puzzle_input)

        row_idx, col_idx = self.map.shape
        self.end_node = (row_idx - 1, col_idx - 1)

    def _parse_input(self, puzzle_input: str) -> np.ndarray:
        return np.array([list(row) for row in puzzle_input.splitlines()], dtype=int)

    def dijkstra(self) -> int:
        starting_node = (0, 0)
        priority_queue = PriorityQueue()
        visited = {starting_node}
        priority_queue.put((0, starting_node))
        while priority_queue:
            current_risk, (current_row, current_col) = priority_queue.get()
            if (current_row, current_col) == self.end_node:
                return current_risk
            for row, col in [
                (current_row + 1, current_col),
                (current_row - 1, current_col),
                (current_row, current_col + 1),
                (current_row, current_col - 1),
            ]:
                if (
                    0 <= row < self.map.shape[0]
                    and 0 <= col < self.map.shape[1]
                    and (row, col) not in visited
                ):
                    weight = self.map[row, col]
                    priority_queue.put((current_risk + weight, (row, col)))
                    visited.add((row, col))


def part_1(puzzle_input):
    cavern = Cavern(puzzle_input)
    return cavern.dijkstra()


def part_2():
    ...


if __name__ == "__main__":
    puzzle_input = Path("2021/15/input.txt").read_text()
    print("Part 1:", part_1(puzzle_input))
