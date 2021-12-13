from collections import defaultdict
from pathlib import Path


class Caves:
    def __init__(self, puzzle_input: str, small_cave_twice: bool) -> None:
        self.paths = self._parse_input(puzzle_input)
        self._build_graph()
        self.paths_visted = self.dfs(
            cave="start",
            visited={"start"},
            small_cave_twice=small_cave_twice,
        )

    def dfs(
        self, cave: str, visited: set, small_cave_twice: bool, counter: int = 0
    ) -> None:
        if cave == "end":
            return 1

        for neighbor_cave in self.graph[cave]:
            if neighbor_cave.isupper():
                counter += self.dfs(neighbor_cave, visited, small_cave_twice)
            else:
                if neighbor_cave not in visited:
                    counter += self.dfs(
                        neighbor_cave, visited | {neighbor_cave}, small_cave_twice
                    )
                elif small_cave_twice and neighbor_cave not in {"start", "end"}:
                    counter += self.dfs(neighbor_cave, visited, small_cave_twice=False)

        return counter

    def _build_graph(self) -> None:
        self.graph = defaultdict(list)
        for start, end in self.paths:
            self.graph[start].append(end)
            self.graph[end].append(start)

    def _parse_input(self, puzzle_input: str) -> list[list[str]]:
        return [row.split("-") for row in puzzle_input.split("\n") if row]


def part_1(puzzle_input: str) -> int:
    caves = Caves(puzzle_input, small_cave_twice=False)
    return caves.paths_visted


def part_2(puzzle_input: str) -> int:
    caves = Caves(puzzle_input, small_cave_twice=True)
    return caves.paths_visted


if __name__ == "__main__":
    puzzle_input = Path("2021/12/input.txt").read_text()
    print("Part 1:", part_1(puzzle_input))
    print("Part 2:", part_2(puzzle_input))
