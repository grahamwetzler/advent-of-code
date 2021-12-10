import re
from pathlib import Path

BRACKETS = {")": "(", "]": "[", "}": "{", ">": "<"}


class Line:
    def __init__(self, line):
        self.line = line

    def parse(self):
        return re.match("\[.*\]", self.line)

    @property
    def first_illegal_bracket(self):
        opening_brackets = []

        for bracket in self.line:
            match bracket:
                case "(" | "[" | "{" | "<":
                    opening_brackets.append(bracket)
                case _ as b:
                    if opening_brackets[-1] == BRACKETS[b]:
                        opening_brackets.pop()
                    else:
                        return b


def parse_input():
    lines = Path("2021/10/input.txt").read_text().split("\n")
    return [p for p in lines if p]


def part_1():
    illegal_characters = []
    scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
    for line in parse_input():
        if bracket := Line(line).first_illegal_bracket:
            illegal_characters.append(bracket)
    return sum([scores[i] for i in illegal_characters])


if __name__ == "__main__":
    print("Part 1:", part_1())
