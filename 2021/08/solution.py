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
        display = Display(entry).find_unique_output()
        for digit in display.digits:
            if digit in UNIQUE_SEGMENTS.keys():
                unique_segments_found += 1

    return unique_segments_found


def part_2():
    values = []
    for entry in parse_input():
        display = Display(entry)
        display.map_input_to_numbers()
        values.append(display.output_value)
    return sum(values)


class Display:
    def __init__(self, entry: Entry):
        self.pattern = entry.pattern
        self.output = entry.output
        self.digits = [None] * 4
        self.pattern_mapping = {p: None for p in self.pattern}

    def find_unique_output(self):
        for idx, value in enumerate(self.output):
            for digit, segments in UNIQUE_SEGMENTS.items():
                if len(value) == segments:
                    self.digits[idx] = digit
        return self

    def map_input_to_numbers(self):
        def patterns_by_length(length) -> list:
            patterns = []
            for p in filter(lambda x: len(x) == length, self.unmapped):
                patterns.append("".join(sorted(list(p))))
            return patterns

        _1 = patterns_by_length(2)[0]
        _4 = patterns_by_length(4)[0]
        _7 = patterns_by_length(3)[0]
        _8 = patterns_by_length(7)[0]

        self.pattern_mapping[_1] = 1
        self.pattern_mapping[_4] = 4
        self.pattern_mapping[_7] = 7
        self.pattern_mapping[_8] = 8

        set_1 = set(_1)
        set_4 = set(_4)

        four_diff = set_4 - set_1

        for p in patterns_by_length(5):
            if set_1.issubset(p):
                self.pattern_mapping[p] = 3
            elif four_diff.issubset(p):
                self.pattern_mapping[p] = 5
            else:
                self.pattern_mapping[p] = 2

        for p in patterns_by_length(6):
            if set_4.issubset(p):
                self.pattern_mapping[p] = 9
            elif four_diff.issubset(p):
                self.pattern_mapping[p] = 6
            else:
                self.pattern_mapping[p] = 0

    @property
    def unmapped(self) -> list[str]:
        return [k for k, v in self.pattern_mapping.items() if v is None]

    @property
    def output_value(self) -> int:
        values = ""
        for pattern in self.output:
            pattern = "".join(sorted(list(pattern)))
            values += str(self.pattern_mapping[pattern])

        return int(values)


if __name__ == "__main__":
    print("Part 1:", part_1())
    print("Part 2:", part_2())
