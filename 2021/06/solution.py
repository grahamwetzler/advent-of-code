from pathlib import Path
from dataclasses import dataclass


def parse_input() -> list:
    puzzle_input = Path("2021/06/input.txt").read_text()
    split = puzzle_input.split(",")
    return [int(n) for n in split]


@dataclass
class Fish:
    timer: int = 8

    def __repr__(self):
        return str(self.timer)

    def day(self):
        self.timer -= 1
        if self.timer < 0:
            self.timer = 6
            return Fish()


def count_fish(days) -> int:
    puzzle_input = parse_input()
    fishes = [Fish(t) for t in puzzle_input]
    for day in range(days):
        new_fishes = []
        for fish in fishes:
            if new_fish := fish.day():
                new_fishes.append(new_fish)
        fishes += new_fishes

    return len(fishes)


if __name__ == "__main__":
    print("Part 1:", count_fish(days=80))
