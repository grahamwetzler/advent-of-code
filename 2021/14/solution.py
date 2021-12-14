from itertools import pairwise
from collections import Counter
from pathlib import Path


class Polymer:
    def __init__(self, puzzle_input: str) -> None:
        self._parse(puzzle_input)
        self.polymer = None

    def _parse(self, puzzle_input: str):
        template, rules = puzzle_input.split("\n\n")
        self.template = template
        # self.rules = {
        #     k: v for rule in rules.split("\n") for k, v in rule.split(" -> ") if rule
        # }
        self.rules = {}
        for rule in rules.split("\n"):
            if rule:
                k, v = rule.split(" -> ")
                self.rules[k] = v

    def insert(self, polymer: str):
        updates = []
        for idx, pair in enumerate(pairwise(polymer), start=1):
            pair = "".join(pair)
            element = self.rules[pair]
            updates.append((element, idx))

        insert_offset = 0
        for element, insert_position in updates:
            insert = insert_position + insert_offset
            polymer = polymer[:insert] + element + polymer[insert:]
            insert_offset += 1

        self.polymer = polymer

        return self.polymer

    def step(self, times: int):
        for _ in range(times):
            polymer = self.template if not self.polymer else self.polymer
            self.insert(polymer)

        return self.polymer


def part_1(puzzle_input):
    polymer = Polymer(puzzle_input)
    counter = Counter(polymer.step(10))
    most_common, *_, least_common = counter.most_common()
    return most_common[1] - least_common[1]


def part_2():
    ...


if __name__ == "__main__":
    puzzle_input = Path("2021/14/input.txt").read_text()
    print("Part 1:", part_1(puzzle_input))
