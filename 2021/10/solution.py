from pathlib import Path
from statistics import median

BRACKETS_OPEN_CLOSE = {"(": ")", "[": "]", "{": "}", "<": ">"}
BRACKETS_CLOSE_OPEN = {v: k for k, v in BRACKETS_OPEN_CLOSE.items()}


class Line:
    def __init__(self, line):
        self.line = line
        self.first_illegal_bracket = None
        self.missing_brackets = None
        self._parse()

    def _parse(self):
        opening_brackets = []

        for bracket in self.line:
            match bracket:
                case "(" | "[" | "{" | "<":
                    opening_brackets.append(bracket)
                case _ as b:
                    if opening_brackets[-1] == BRACKETS_CLOSE_OPEN[b]:
                        opening_brackets.pop()
                    else:
                        self.first_illegal_bracket = b
                        return self

        self.missing_brackets = [BRACKETS_OPEN_CLOSE[b] for b in opening_brackets[::-1]]
        return self


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


def part_2():
    missing_bracket_scores = []
    scores = {")": 1, "]": 2, "}": 3, ">": 4}
    for line in parse_input():
        if missing := Line(line).missing_brackets:
            score = 0
            for m in missing:
                score *= 5
                score += scores[m]

            missing_bracket_scores.append(score)

    return median(missing_bracket_scores)


if __name__ == "__main__":
    print("Part 1:", part_1())
    print("Part 2:", part_2())
