from collections import namedtuple
from pathlib import Path

Entry = namedtuple("Entry", ["pattern", "output"])

UNIQUE_SEGMENTS = {1: 2, 4: 4, 7: 3, 8: 7}


def parse_input():
    puzzle = Path("2021/08/input.txt").read_text().split("\n")
    entry_list = []
    for entry in puzzle:
        if not entry:
            break
        pattern, output = entry.split(" | ")
        entry_list.append(Entry(pattern.split(), output.split()))
    return entry_list


def part_1():
    unique_segments_found = 0
    for entry in parse_input():
        display = Display(entry).find_unique()
        for digit in display.digits:
            if digit in UNIQUE_SEGMENTS.keys():
                unique_segments_found += 1

    return unique_segments_found


class Display:
    def __init__(self, entry):
        self.pattern = entry.pattern
        self.output = entry.output
        self.digits = [None] * 4

    def find_unique(self):
        for idx, value in enumerate(self.output):
            for digit, segments in UNIQUE_SEGMENTS.items():
                if len(value) == segments:
                    self.digits[idx] = digit
        return self


if __name__ == "__main__":
    print("Part 1:", part_1())
