from collections import defaultdict
from pathlib import Path


class Caves:
    def __init__(self, puzzle_input) -> None:
        self.paths = self._parse_input(puzzle_input)
        self._build_graph()
        self.paths_visted = self.dfs(cave="start", visited={"start"})

    def dfs(self, cave, visited, counter=0) -> None:
        if cave == "end":
            return 1

        for neighbor_cave in self.graph[cave]:
            if neighbor_cave.isupper():
                counter += self.dfs(neighbor_cave, visited)
            elif neighbor_cave not in visited:
                counter += self.dfs(neighbor_cave, visited | {neighbor_cave})

        return counter

    def _build_graph(self) -> None:
        self.graph = defaultdict(list)
        for start, end in self.paths:
            self.graph[start].append(end)
            self.graph[end].append(start)

    def _parse_input(self, puzzle_input) -> list[list[str]]:
        return [row.split("-") for row in puzzle_input.split("\n") if row]


def part_1(puzzle_input):
    caves = Caves(puzzle_input)
    return caves.paths_visted


if __name__ == "__main__":
    puzzle_input = Path("2021/12/input.txt").read_text()
    print("Part 1:", part_1(puzzle_input))
