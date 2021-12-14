from collections import Counter
from itertools import pairwise
from pathlib import Path


class Polymer:
    def __init__(self, puzzle_input: str, steps: int) -> None:
        self._parse(puzzle_input)
        self.pairs = Counter()
        self.elements = Counter(self.template)

        for pair in pairwise(self.template):
            pair = "".join(pair)
            self.pairs[pair] += 1

        self.step(steps)

    def _parse(self, puzzle_input: str) -> None:
        puzzle_input = puzzle_input.splitlines()
        self.template = puzzle_input[0]
        self.rules = {
            k: v for k, v in (rule.split(" -> ") for rule in puzzle_input[2:])
        }

    def step(self, steps: int) -> "Polymer":
        for _ in range(steps):
            for pair, count in list(self.pairs.items()):
                self.pairs[pair] -= count

                insert = self.rules[pair]
                self.pairs[pair[0] + insert] += count
                self.pairs[insert + pair[1]] += count
                self.elements[insert] += count

        return self

    @property
    def max(self) -> int:
        return max(self.elements.values())

    @property
    def min(self) -> int:
        return min(self.elements.values())


def day_14(puzzle_input: str, steps: int) -> int:
    polymer = Polymer(puzzle_input, steps)
    return polymer.max - polymer.min


if __name__ == "__main__":
    puzzle_input = Path("2021/14/input.txt").read_text()
    print("Part 1:", day_14(puzzle_input, 10))
    print("Part 2:", day_14(puzzle_input, 40))
